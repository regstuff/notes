#!/usr/bin/env python3
"""Check a lecture-notes markdown file before handing it over.

Usage: python3 check_notes.py NOTES.md [--anchors]

1. Source checks for things that break Python-Markdown + pymdownx.arithmatex, the standalone rule,
   and figure numbering. Each finding is printed with its line number.
2. A strict MkDocs build of the file in a temporary project that copies the user's config
   (Material theme, toc permalinks, arithmatex generic) and adds `validation: links: anchors: warn`,
   so a link to a missing #section fails the build. Without that setting MkDocs only logs it.
3. Checks of the built HTML: stray $ outside math, LaTeX leaking into text, h5+ headings.

--anchors prints every heading with the id MkDocs gives it, to copy into back-links.

MkDocs runs from the .venv folder inside this skill's folder. If that venv is missing or broken
(for example after the skill folder was copied somewhere else), it is rebuilt and mkdocs-material
installed into it, which needs network access once.
Exit status is 1 if the build fails or any error-level finding is reported.
"""
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

VENV = Path(__file__).resolve().parent.parent / ".venv"  # the skill's own venv; never install elsewhere
CONFIG = """site_name: Check
theme:
  name: material
plugins:
  - search
markdown_extensions:
  - toc:
      permalink: true
  - pymdownx.arithmatex:
      generic: true
validation:
  links:
    anchors: warn
"""
LIST_ITEM = re.compile(r"^\s*([-*+]|\d+[.)])\s+")
INLINE_MATH = re.compile(r"(?<![\\$])\$(?!\$)(.+?)(?<![\\$])\$(?!\$)")
CODE_SPAN = re.compile(r"`[^`]*`")
BOOK_REF = re.compile(
    r"\b(the|this|our) (text)?book\b|\btextbook\b|\bexercises?\b"
    r"|\b(Chapter|Section|Theorem|Lemma|Proposition|Corollary|Definition|Exercise|Problem|Equation|Eq\.|Page|p\.)\s?\d",
    re.I,
)
LATEX_LEAK = re.compile(r"\\(frac|mathrm|mathcal|mathbb|sqrt|alpha|beta|gamma|Omega|Lambda|langle|times|cdot)\b")

errors, warnings = [], []


def err(n, msg):
    errors.append(f"line {n}: {msg}")


def warn(n, msg):
    warnings.append(f"line {n}: {msg}")


def source_checks(lines):
    in_code = in_display = False
    prev = ""
    for n, line in enumerate(lines, 1):
        if line.lstrip().startswith("```"):
            in_code = not in_code
            prev = line
            continue
        if in_code:
            prev = line
            continue
        stripped = CODE_SPAN.sub("", line)
        if re.match(r"^#{5,}\s", line):
            err(n, "heading deeper than ####; use a bold lead-in instead")
        starts_block = LIST_ITEM.match(line) or line.startswith("|")
        prev_in_block = LIST_ITEM.match(prev) or prev.startswith("|") or prev.startswith((" ", "\t"))
        if starts_block and prev.strip() and not prev_in_block and not in_display:
            err(n, "list or table needs a blank line before it")
        if "$$" in stripped:
            if LIST_ITEM.match(line) or line.startswith((" ", "\t")) or (LIST_ITEM.match(prev) and not in_display):
                err(n, "display math inside a list item; move it out of the list")
            if stripped.count("$$") % 2:
                in_display = not in_display
        singles = len(re.findall(r"(?<![\\$])\$(?!\$)", stripped))
        if not in_display and "$$" not in stripped and singles % 2:
            err(n, "odd number of $ on this line: a math span is not closed (or a $ needs escaping as \\$)")
        elif not in_display and "$$" not in stripped:
            for m in INLINE_MATH.finditer(stripped):
                body, end = m.group(1), m.end()
                if body != body.strip():
                    err(n, f"space just inside $...$: {m.group(0)[:40]}")
                if end < len(stripped) and stripped[end].isdigit():
                    err(n, f"closing $ followed by a digit: {stripped[m.start():end + 3]}")
        for url in re.findall(r"\]\((\S*?\([^)\s]*\)\S*?)\)", stripped):
            err(n, f"parentheses in URL, percent-encode them as %28 %29: {url}")
        if "\u2014" in stripped:
            warn(n, "em dash")
        if not line.startswith("*Figure") and (m := BOOK_REF.search(stripped)):
            warn(n, f"possible textbook reference, notes must stand alone: '{m.group(0)}'")
        prev = line


def figure_checks(lines):
    text = "\n".join(lines)
    captions = [int(x) for x in re.findall(r"^\*Figure (\d+)\.", text, re.M)]
    if not captions:
        return
    if captions != list(range(captions[0], captions[0] + len(captions))):
        errors.append(f"figures: captions not consecutive: {captions}")
    body = re.sub(r"^\*Figure \d+\..*$", "", text, flags=re.M)
    cited = {int(x) for x in re.findall(r"Figures? (\d+)", body)}
    cited |= {int(b) for a, b in re.findall(r"Figures \d+ and (\d+)", body)}
    for f in captions:
        if f not in cited:
            warnings.append(f"figures: Figure {f} is never mentioned in the text")
    for f in sorted(cited - set(captions)):
        errors.append(f"figures: text mentions Figure {f}, which has no caption")


def term_order_checks(lines):
    # The notes bold a term where they define it. Warn when such a term already appears in the
    # prose above its definition: the reader meets the word before being told what it means.
    # Bold at the start of a line is a lead-in or block title, not a definition, so it is skipped.
    # A term is not flagged if an earlier mention links forward to its definition, or if it is listed
    # in a hidden comment such as <!-- terms checked: scale factor; metric --> (reviewed by hand:
    # glossed where first used, known from the background, or a false alarm).
    # Compare terms with their maths removed and spaces collapsed, so a comment can name
    # "generalized $n$-gon" and match the bolded term however its maths is written.
    def norm(t):
        return " ".join(re.sub(r"\$[^$]*\$", " ", t).split()).lower()

    checked = set()
    for block in re.findall(r"<!--\s*terms checked:(.*?)-->", "\n".join(lines), re.S | re.I):
        checked |= {norm(t) for t in block.split(";") if t.strip()}
    prose, links, in_code = [], [], False
    for n, line in enumerate(lines, 1):
        if line.lstrip().startswith("```"):
            in_code = not in_code
        if in_code or line.lstrip().startswith(("```", "#", "![", "*Figure", "<!--")):
            prose.append((n, ""))
            continue
        links += [(n, norm(t)) for t in re.findall(r"\[([^\]]*)\]\([^)]*\)", line)]
        # drop maths, code and whole links from the prose that is searched
        text = re.sub(r"\$\$.*?\$\$|\$[^$]*\$|`[^`]*`|\[[^\]]*\]\([^)]*\)", " ", line)
        prose.append((n, text))
    seen = set()
    for n, text in prose:
        body = re.sub(r"^\s*(?:>\s*)?(?:[-*+]\s+|\d+[.)]\s+)?\*\*[^*]+\*\*", "", text)
        for term in re.findall(r"\*\*([^*$]{3,40})\*\*", body):
            key = norm(term)
            if key in seen or len(key.split()) > 5 or key.endswith((".", ":", "?")) or len(key) < 6:
                continue
            seen.add(key)
            if key in checked or any(m < n and key in t for m, t in links):
                continue
            words = r"\s+".join(re.escape(w) for w in key.split())
            pattern = re.compile(r"\b" + words + r"(?:s|es)?\b", re.I)
            for m_line, earlier in prose:
                if m_line >= n - 5:  # a lead-in sentence just above the definition is fine
                    break
                if pattern.search(earlier.replace("**", "")):
                    warn(n, f"'{term.strip()}' is defined here but already used on line {m_line}")
                    break


def ensure_mkdocs():
    # Run everything as `python -m`, because the scripts in .venv/bin have the venv's absolute path
    # in their first line and stop working when the skill folder is copied or moved.
    python = VENV / "bin" / "python"
    probe = [str(python), "-c", "import mkdocs, material, pymdownx"]
    if python.exists() and subprocess.run(probe, capture_output=True).returncode == 0:
        return [str(python), "-m", "mkdocs"]
    print(f"Setting up MkDocs in {VENV} ...", file=sys.stderr)
    shutil.rmtree(VENV, ignore_errors=True)
    subprocess.run([sys.executable, "-m", "venv", str(VENV)], check=True)
    subprocess.run([str(python), "-m", "pip", "install", "-q", "mkdocs-material"], check=True)
    return [str(python), "-m", "mkdocs"]


def build(md_path, lines, show_anchors):
    mkdocs = ensure_mkdocs()
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        docs = tmp / "docs"
        docs.mkdir()
        (tmp / "mkdocs.yml").write_text(CONFIG)
        shutil.copy(md_path, docs / "index.md")
        for rel in set(re.findall(r"!\[[^\]]*\]\(([^)\s]+)\)", "\n".join(lines))):
            if rel.startswith("http"):
                continue
            src = md_path.parent / rel
            if src.exists():
                (docs / rel).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(src, docs / rel)
            else:
                errors.append(f"image not found: {rel}")
        # sibling pages linked as other.md#anchor, so the build can check those anchors too
        for rel in set(re.findall(r"\]\(([^)#\s:]+\.md)(?:#[^)]*)?\)", "\n".join(lines))):
            src = (md_path.parent / rel).resolve()
            if src.exists() and src != md_path:
                (docs / rel).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(src, docs / rel)
        run = subprocess.run(mkdocs + ["build", "--strict"], cwd=tmp, capture_output=True, text=True)
        for msg in re.findall(r"^(?:WARNING|ERROR)\s+-\s+(.*)$", run.stderr, re.M):
            errors.append(f"build: {msg}")
        if run.returncode != 0 and not errors:
            errors.append("build failed:\n" + run.stderr[-2000:])
        html_path = tmp / "site" / "index.html"
        if not html_path.exists():
            return
        html = html_path.read_text()
    body = html.split("<article", 1)[-1]
    ids = re.findall(r'<h([1-4]) id="([^"]+)"[^>]*>(.*?)<a class="headerlink"', body, re.S)
    nomath = re.sub(r'<(span|div) class="arithmatex">.*?</\1>', "", body, flags=re.S)
    text = re.sub(r"<[^>]+>", "", re.sub(r"<(code|pre)\b.*?</\1>", "", nomath, flags=re.S))
    if "$" in text:
        snippets = [text[max(0, i - 30):i + 30].replace("\n", " ") for i in [m.start() for m in re.finditer(r"\$", text)][:5]]
        errors.append(f"{text.count('$')} stray $ outside math in the built page, e.g. {snippets}")
    if leaks := LATEX_LEAK.findall(text):
        errors.append(f"LaTeX outside math in the built page: {sorted(set(leaks))}")
    if re.search(r"<h[5-6]", body):
        errors.append("built page has h5/h6 headings")
    linked = set(re.findall(r'<a href="#([^"]+)"', body))  # headerlinks put class= first
    for _, hid, _ in ids:
        if re.search(r"_\d+$", hid) and hid in linked:
            warnings.append(f"link to #{hid}: a duplicate heading name, so the id shifts if a same-named heading is added above it; rename the heading")
    if show_anchors:
        print("Heading ids (link with [text](#id)):")
        for level, hid, title in ids:
            plain = re.sub(r"<[^>]+>", "", title).strip()
            print(f"  {'  ' * (int(level) - 1)}#{hid}   {plain}")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        sys.exit(__doc__)
    md_path = Path(args[0]).resolve()
    lines = md_path.read_text().splitlines()
    source_checks(lines)
    figure_checks(lines)
    term_order_checks(lines)
    build(md_path, lines, "--anchors" in sys.argv)
    for title, items in (("ERRORS", errors), ("WARNINGS (review by hand)", warnings)):
        print(f"{title}: {len(items)}")
        for item in items:
            print("  " + item)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
