# Writing markdown that renders on the user's MkDocs site

Read this before writing the first file of a session. The notes are published with MkDocs Material on GitHub Pages.

## The user's configuration

```yaml
theme:
  name: material
plugins:
  - search
markdown_extensions:
  - toc:
      permalink: true
  - pymdownx.arithmatex:
      generic: true
extra_javascript:
  - javascripts/mathjax.js
  - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js
extra_css:
  - stylesheets/extra.css
validation:
  links:
    anchors: warn   # added October 2026: broken #section links are reported
```

There is no `admonition`, `pymdownx.details`, `footnotes`, `attr_list` or `md_in_html`. So:

- No `!!! note` boxes, collapsible `???` blocks or footnotes. Asides and Notes are set off with `---` rules and a bold title (see SKILL.md).
- Markdown inside raw HTML is not processed, so don't wrap content in `<div>`.
- Mermaid is not set up. Draw diagrams as images or as plain text in fenced code blocks.

## Maths

Python-Markdown parses the page first and arithmatex picks out the maths, so some markdown that looks fine breaks. Each of these broke rendering in earlier notes:

| Problem | Bad | Good |
| --- | --- | --- |
| A list or table straight after a paragraph is read as part of the paragraph | `text`, then `- item` on the next line | Put a blank line before every list and table |
| Display maths inside a list item is not picked up | `- item` followed by an indented `$$...$$` | End the list, put the `$$` block after it, and continue in prose |
| A closing `$` followed straight away by a digit is not read as closing | `$x$2` | `$x$ 2`, or `$x_2$` |
| A space just inside the dollars stops it being maths | `$ x$`, `$x $` | `$x$` |
| An unclosed `$` swallows the text after it | `a line $K ($\dim k = 1$)` | `a line $K$ ($\dim k = 1$)` |
| A literal dollar sign | `costs $5` | `costs \$5` |
| Parentheses in a URL end the link early | `(https://doi.org/10.1016/0370-2693(82)90107-2)` | `(https://doi.org/10.1016/0370-2693%2882%2990107-2)` |

`$\Lambda$CDM`, with a letter straight after the closing `$`, is fine.

Write display maths as a `$$` block on its own lines with a blank line above and below. Use `\begin{aligned}` inside `$$` for multi-line derivations. MathJax 3 handles standard LaTeX maths and `\mathcal`, `\mathbb`, `\boldsymbol`, `\operatorname`. Don't define macros with `\newcommand`. Spell commands out so that each formula can be read on its own.

## Headings and anchors

- One `#` title per file. Then `##`, `###`, `####`. Nothing deeper (the user's rule; it keeps the contents sidebar readable). Use a bold lead-in paragraph instead.
- The toc extension gives each heading an id: lowercase, spaces become hyphens, punctuation is dropped, and LaTeX loses its backslashes and braces. So `### The one-or-all axiom` becomes `#the-one-or-all-axiom` and `### $\mathcal{Q}$-lines` becomes `#mathcalq-lines`.
- A repeated heading gets `_1`, `_2`, ... in order down the page. Eleven chapters with a `### Summary` each give `#summary`, `#summary_1`, ... `#summary_10`, and inserting a chapter shifts all of them. Give any section you link to a distinctive heading, and keep maths out of headings that are link targets.
- Link to a section on the same page with `[the one-or-all axiom](#the-one-or-all-axiom)`. Link to another page with a relative path, `[polar spaces](maths_3_projective_geometry.md#polar-spaces-polarity)`.
- Don't guess ids. Run `check_notes.py --anchors` to print every heading's id.
- MkDocs only logs a broken `#anchor` by default. The `validation` setting above makes it a warning, and the checker's strict build turns that warning into a failure.

## Figures

```markdown
![Short alt text describing the image](figures/chapter_topic_name.png)

*Figure 7. Self-contained caption: what is plotted, what each panel shows as (a), (b), where the data come from.*
```

- Number figures continuously through the whole file, never per chapter. Inserting a figure means renumbering every later caption and every "Figure N" in the text.
- Keep images in `figures/` next to the markdown file. Name them `<chapter>_<what>.png` so a combined file stays manageable.
- Make each figure with a Python script saved beside the notes, for example `scripts/<subject>/make_<chapter>_figures.py`. The script takes the output directory, and any data file path, as arguments. A figure that can't be regenerated can't be fixed later.

## The checker

```bash
python3 <skill folder>/scripts/check_notes.py path/to/notes.md [--anchors]
```

The script:

- checks every pitfall in the maths table above, line by line;
- checks the heading depth, the figure numbering and that each figure is mentioned in the text;
- warns about em dashes, anything that looks like a reference to the textbook, and terms that the notes define in **bold** but use earlier (see `gap-checks.md`);
- runs a strict MkDocs build with broken anchors turned into failures, then checks the built page for stray `$` and LaTeX leaking out of maths.

The checker runs MkDocs from the `.venv` folder in the skill's folder. On the first run, or whenever that venv is missing or broken (for example after the skill folder has been copied somewhere else), it rebuilds the venv and installs `mkdocs-material`. This needs network access and takes about half a minute. The checker leaves out the user's `extra_javascript` and `extra_css`, which don't affect the HTML.

Treat the warnings as things to check by hand. "Exercise" in ordinary prose may be fine; a chapter or section number never is.
