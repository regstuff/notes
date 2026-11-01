---
name: lecture-notes
description: Write streamlined, intuition-first lecture notes in Markdown with LaTeX (rendered by MkDocs Material + arithmatex on GitHub Pages) for the user to read before a textbook chapter, paper or topic in mathematics or physics. The notes are expository like Clayton's Principles of Stellar Evolution, built on the reader's background, with worked examples, asides and on-the-spot Notes. Use this whenever the user asks for lecture notes, study notes, pre-reading, a primer, a companion to a chapter, or "notes so the chapter is easier to read", or wants a chapter, theorem cluster or topic taught in writing. Also use it when continuing, revising, reviewing or fixing an existing set of lecture notes, even if the user doesn't say "lecture notes".
---

# Lecture notes for learning mathematics and physics

The reader studies these notes *before* the chapter, so that the chapter reads easily afterwards. The notes cover what the chapter covers, with different priorities: the picture first, the motivation always, and the formalism in service of the picture. The model is Donald Clayton's *Principles of Stellar Evolution and Nucleosynthesis*. It is rigorous in its physics and mathematics, but written so that the reader comes away with a feel for the subject and not just its equations.

The reader is the user, or students the user is writing for. Everything below serves one goal: at no point should the reader be lost, bored, or left holding a formula with no picture behind it.

## Before writing

Collect what's missing in one round of questions; don't ask about what you already know.

1. **The reader's background.** You need an accurate map of it for two reasons. Every term must either be known to the reader or defined in the notes. And the asides should connect the new topic to what the reader already knows. Take the core, non-elective mathematics and physics of an undergraduate physics degree as known, unless the list below says otherwise. Beyond that core, the reader has studied:

   - **Algebra:** a basic course on sets, rings, fields and basic group theory, including the basics of representation theory, permutation groups and group actions (P. J. Cameron's *Introduction to Algebra*, plus extra notes). Includes irreducible polynomials, and commutants (matrices commuting with every representation matrix) from group theory. Knows the sporadic simple groups, such as the Mathieu groups, only by name.
   - **Projective geometry:** a basic course using Johannes Ueberberg's *Foundations of Incidence Geometry: Projective and Polar Spaces*, skipping pseudo-quadrics.
   - **Thermal physics:** Daniel Schroeder's *An Introduction to Thermal Physics*.
   - **Quantum information and quantum theory:** Nielsen and Chuang's *Quantum Computation and Quantum Information*, focusing on the quantum theory and skipping the algorithms, plus its chapter on quantum error correction (stabilizer codes).
   - **Quantum physics:** a one-quarter course built on state vectors, bra–ket notation and density matrices.
   - **General relativity:** a course up to the Schwarzschild metric, covering neither gravitational waves nor cosmology.
   - **Stellar structure:** Onno Pols' lecture notes.

   Known gaps (explain these in place if used): tight-binding models, Markov-chain generators, quantum contextuality (Mermin–Peres), perfect and inseparable field extensions, and the projective picture of the light cone as a celestial sphere. The minimal polynomial of a matrix is not in the list (the reader knows irreducible polynomials); recall it where needed.

   Ask only about prerequisites of the new topic that this list doesn't settle. When the user reports new study, add it to this list, so that the record travels with the skill.
2. **The source.** Get the chapter itself (PDF path and pages) and any reading notes or formula sheets the user has. Read the whole chapter before writing the first line, because each section's overview has to know where the section is going. While reading:
   - list the errors you find (see "Accuracy" below for how to handle them);
   - note the textbook's conventions wherever texts differ, such as left or right vector spaces, the metric signature, or which slot of a sesquilinear form carries the automorphism.

   If you can't tell which convention the textbook uses, because you don't have the text or it isn't clear, ask before writing.

   **Cut the book into chapter PDFs.** When the user gives a whole book and the list of sections they want, first cut one PDF per chapter that holds only those sections, and write each chapter from its own PDF. The user reads these PDFs too, so put them where the user will find them: in a folder beside the book, named after it, such as `debruyn_chapters/debruyn_ch2.pdf`. Keep every page of a wanted section whole, including a page where it ends and the next section begins. Add a `sections.md` to the folder giving, for each PDF, its chapter, its sections with their titles, and its printed and PDF page numbers. Printed page numbers differ from PDF page numbers, and the difference can change from chapter to chapter, so read the printed number off each page with `pdftotext` instead of adding a fixed offset. Poppler's `pdfseparate` and `pdfunite` do the cutting.

   **Use the whole book when the chapter PDF is not enough.** The wanted sections sometimes rely on something outside them: a definition, a result or a piece of notation from a section that was cut. Look it up in the whole book rather than guessing. If a review finds a mistake that came from missing context, redo that part with the whole book. Either way, the list of sections in `sections.md` still decides what the notes cover; the rest of the book is only for looking things up.
3. **The output.** The notes are one file. Every chapter goes into the same file, unless the user says otherwise. Ask where the file lives and where figures and scripts go. If the file already exists, match its conventions: heading case, block formats, figure numbering.

   **Name the file and title from the subject and its number.** The user numbers their notes by subject: "physics file number 6 on stellar evolution", "maths 4, incidence geometry". Two examples:

   - Physics file 6 on stellar evolution: the file is `physics_6_stellar_evolution.md` and its title line is `# Physics 6 - Stellar Evolution`.
   - Maths file 4 on incidence geometry: the file is `maths_4_incidence_geometry.md` and its title line is `# Maths 4 - Incidence Geometry`.

   The file name is lowercase with underscores. The title capitalises the subject and each main word of the topic, with a spaced hyphen after the number. If the user hasn't given the subject, the number or the topic name, ask.
4. **What the notes already cover.** Before writing a chapter, find out what the notes already define, so that the chapter doesn't define anything a second time. This is easy to miss when each chapter is written from its own PDF, and it has happened. Look in this order:

   - the user's notes file, such as `maths_4_incidence_geometry.md`. It is the record, because the user edits it and their version is what the reader reads;
   - earlier chapters that are written but not yet merged into that file, in their own files;
   - if there is no notes file yet, the files of the earlier chapters.

   Don't read them from end to end. List their headings and the terms they define with `check_notes.py --terms <files>`, then read in full the sections the new chapter builds on. Note the symbols they use and keep using them. When the chapter needs a term that is already defined, link back to it instead of defining it again (see your subject's section). Before handing over, run the checker with `--earlier` on the same files to catch any that slipped through.

Write one chapter at a time and hand it over for review before starting the next. The user's corrections on one chapter usually apply to every later one, so record them and apply them from then on.

## Planning the notes

Before writing a new set of notes, show the user a content plan. For each source section, list the notes subsections, and for each subsection give 1-3 lines that the user can judge:

- **The order of ideas.** Write the line as a sequence (idea, idea, example, ...), not a bag of terms. Every idea comes before the example that relies on it.
- **The purpose of every unit.** For an example, say what the reader should notice. For a result, say what question it answers and what it is used for later. For a definition, say why it has its shape. That something appears later in the book is not a purpose.
- **Plain words.** The first time the plan names an object or uses a technical term, add a few words of explanation. The user can't judge a plan that relies on jargon they haven't met. For prerequisites that aren't obvious, say where they come from: an earlier section, or which part of the background.

Run the gap checks in `references/gap-checks.md` on the plan before showing it. The checklist covers names used before their objects, jargon, hooks that need later machinery, unstated prerequisites, units without a purpose, ideas out of order, material moved earlier than the source, and further kinds: tools far from their payoff, missing roadmaps, notation, wording that differs from the textbook, density, size, pictures, unkept promises, and hard passages in the textbook. If other agents are helping with the plan, ask them to run the same checks independently, and run them yourself too.

## Which content section applies

The content guidance below is split by subject, and each half is being reworked with the user separately. Use the physics section for a physics file (`physics_N_...`) and the mathematics section for a maths file (`maths_N_...`). Mathematics that appears inside a physics chapter follows the physics section. Everything outside these two sections, from "Before writing" to "Before handing over", applies to both subjects.

## Physics

The sections below are the content guidance as it stood before the split, kept unchanged for now. They will be reworked with the user in the same way as the mathematics section.

### How a section is built

**Open with why.** Start each section with a short overview and motivation: what problem it solves, where it is heading, and what the reader gains, for this topic and for mathematics or physics more widely. Do the same for any run of results heading to one destination, such as a cluster of lemmas leading up to the one-or-all axiom, not only for headed sections. Make the opening a question, a puzzle or a promise of a payoff. Don't write a table of contents in prose ("In this section we will...").

**Then the picture, then the formalism.** Give the reader something to hold in their mind before the symbols arrive. This can be a physical image, a familiar object, or the smallest example.

**Introduce terms where they are used.** Define each new term the first time it appears, at the point where it's needed. Two or three definitions can go together if they are used together straight away. Never front-load a list of definitions: the reader can't hold terms that have no job yet. Reread each paragraph and ask whether it uses a word this reader hasn't met. When a word turns out to be undefined, including informal labels such as "short cycles", "extreme" or "rigid", fix it by defining it where it first appears. Don't paraphrase the word away: the reader will meet it again, in the notes or in the book.

**Build in order.** Each section should rest only on what comes before it. If a later idea is needed early, give a one-line working version and link forward to where it is done properly.

**Summarise sparingly.** Close a section with a summary only where several separate threads came together, or where the summary gives a different way of looking at things. Most sections don't need one.

### Making it intuitive

**Give examples, so the mathematics isn't abstract.** Construct an instance and test it. For polar spaces, write down a symplectic form, check that it is alternating, and find its totally isotropic lines. The smallest nontrivial finite case, worked in full, is often the best example there is.

**Show more than one view of the same object.** For example, show it projectively, as an affine slice, over the reals and over a finite field. Seeing that two familiar things are one object is often the moment the idea clicks.

**Explain why each definition has its shape.** Say what would go wrong with the obvious alternative. For example, if lines lying inside the quadric didn't count as tangents, the tangent plane would have lines missing from it.

**Answer the reader's objection before they raise it.** When a construction looks arbitrary, say so and resolve it. For example: "Doesn't this depend on which form we chose?" No: over a finite field, all nondegenerate forms of one type are equivalent.

**Show what breaks.** Drop a hypothesis, or try the next case up, and show the failure. A cubic surface can't satisfy the one-or-all axiom, and seeing why says more about the axiom than restating it does.

**In physics, put in real numbers:**

- an order-of-magnitude estimate, such as how many CMB photons are in this room;
- a check of limiting cases and units after each result;
- a named misconception, corrected directly.

**Do it for the reader.** Don't set exercises or say "try this". If doing something would be illuminating, do it in full in the text. If the source has check-yourself questions worth keeping, turn them into Notes and answer them on the spot.

### Going deeper and connecting

**Add asides beyond the source,** short dives chosen to intrigue. Good subjects:

- a link to the reader's background: symplectic forms as phase-space area, polar spaces and quantum error-correcting codes, or the general relativity that a Newtonian derivation skips;
- a modern result, or a historical twist.

The main text must never depend on an aside, so the reader can skip any of them.

**Link back when an earlier idea returns.** Make the link a hyperlink to the section where the idea was introduced, for example `[the one-or-all axiom](#one-or-all-axiom)`. A sentence reminding the reader what it said is often worth including alongside the link. Don't re-derive it. See `references/mkdocs-rendering.md` for how anchors are formed, and print the real ids with the checker rather than guessing.

**Use a table when several things are compared on the same features,** such as the three classical families of polar spaces, or matter, radiation and Λ. A contrast between two things, or one that needs explaining, usually reads better as prose.

## Mathematics

The user supplies the source content. For each chapter, give the plain-English version of the theorems, the definitions and the rest of the chapter, so that it is easy to understand what the author is saying when the user then reads the source. This is not a rule against mathematical notation. The idea is to put each theorem across in easy-to-read language; if it helps, also state the theorem in the usual formal fashion.

**What plain English means.** It is not the textbook's sentence with a few friendly words swapped in, and it is not casual talk with the notation and names taken out. Both of those have happened. Start from what the object looks like or how it is built, in the order the reader would picture it, and attach the book's symbols and parameters to that picture as labels. Don't let symbolic shorthand do the explaining: instead of reading $L_i \setminus \{p\}$ aloud, say what it means in the picture. There is nothing wrong with terminology if it is clearly explained immediately after or below, so keep the standard names (downward heredity, anti-flag, collinearity graph) and explain each one in the same sentence or the next. The plain version must keep every condition of the formal statement, such as "of order $(s, t)$", "nondegenerate" or "$\mu > 0$"; when exactness matters, give the formal statement after it. Compare a textbook paraphrase:

> Let $k_1, \dots, k_s$ be $s \ge 2$ integers, each at least $2$. A $(k_1, \dots, k_s)$-star is a linear space with a point $p$ incident with $s$ lines $L_1, \dots, L_s$, where $L_i$ contains exactly $k_i$ points, such that every line not through $p$ contains exactly two points.

with the plain-English version:

> A $(k_1, k_2, \dots, k_s)$-star is a linear space built around a central hub point $p$ from which $s$ rays (lines) radiate outward. There are $s$ main lines meeting at the hub $p$. The first line has $k_1$ points in total (including $p$), the second has $k_2$ points, and so on up to $k_s$ points. No two of these rays share any points other than $p$, and there are no other points anywhere in the space. Because this is a linear space, every pair of points must be connected by a unique line. Points lying on the same ray are already connected by that ray. To connect two points that lie on different rays, we simply draw a two-point line (a thin line) directly between them. None of these connecting lines contain a third point.

**Give the notation.** For definitions, and in other places where it matters, be sure to mention the notation of the defined item. For example, strongly regular graphs are denoted $SRG(v, k, \lambda, \mu)$: say so, and explain what each of those parameters is. The reader should become familiar with the important notation of the topic from these notes while reading the relevant material in them.

**Combine a clump that tells one story.** Whenever a clump of theorems or definitions tells one coherent story, combine them into one explanation if that helps the reader.

**Say what is implicit.** A theorem or concept often includes information implicitly that isn't immediately obvious. Two examples. In the diagram of a polar space, taking the residue of the highest-dimensional node gives a projective space. For a symplectic form, since all points of the ambient space satisfy the form, what distinguishes the geometry from the ambient space is the lines: the ones that are totally isotropic and the ones that are not. Such insights and perspectives are welcome. But try not to refer to things that will be covered in later chapters, because the reader won't have the context; stick to the matter at hand, or to what came before.

**Build the story.** The focus is not on simply presenting the list of theorems. The focus is on building the "story" of the topic.

**Skip nothing.** Do not skip anything in the given source content unless instructed to.

A few things to keep in mind:

- Give and work out examples, so the mathematics isn't so abstract. For example, when teaching polar spaces, students were actually given examples of constructing a symplectic form and testing its properties.
- Give the motivation behind why we are looking at something, say a subsection or a clump of related theorems, so that the reader gains context before diving in.
- It may also help to summarise a section or subsection where many diverse threads are present, though use this sparingly.
- Wherever different things are compared, tables can be used. Again, this is not a rule; use your judgement about what is reader-friendly.
- Do not explain things such that the reader suddenly encounters terminology they are unfamiliar with. Make sure the notes build up to each point. Where new terms are introduced that the reader may not know, add a definition. It is fine to clump two or three definitions together if they are going to be used together straight away.
- When a term, result or piece of notation from an earlier chapter comes back, do not define it again. Link back to the section where it was introduced, and add a sentence reminding the reader what it means if that was a while back. If the source now defines it more generally or differently, say how the new version relates to the earlier one. "What the notes already cover" under "Before writing" says how to find what is already defined.
- The notes are standalone. Never mention the textbook's section numbers or theorem numbers. The textbook is accompanying learning material and may change, so it must not be load-bearing.
- Do not give exercises or do-it-yourself prompts. Where doing something would be illuminating, actually do it fully for the reader.
- Use figures wherever they illustrate something better than text, or help the reader visualise or intuitively understand something.
- Do not use exclamation marks in the prose. The notes are read on a reader that is not very wide, so keep indentation shallow, and use numbered or bulleted lists only where they help clarity; otherwise write paragraphs.

<!-- Mathematics section changelog. One line per round: date, what was added or changed, and the chapter or problem that prompted it.
2026-11-01: section created from the owner's instructions, replacing the earlier "Mathematics: tell the story" and "Model notes to learn from" sections.
2026-11-01: added "What plain English means" (textbook paraphrase and casual over-correction, keep terms and conditions, star example in the owner's wording) and the no-exclamation-marks, shallow-indentation, few-lists rule, from the De Bruyn chapter 2 rewrite.
2026-11-01: added the bullet on not defining again what an earlier chapter defined, after Gemini's De Bruyn chapter 3 and 4 notes redefined terms already in maths_4. The shared "Before writing" steps also gained chapter PDFs cut by section (whole book for lookups) and "What the notes already cover"; the checker gained --terms and --earlier.
-->

## Block formats

The site has no admonition boxes, so set blocks off with horizontal rules and a bold title.

An **Aside** is a deeper dive the reader can skip:

```markdown
---

**Aside: neutrino oscillations are a precessing qubit.**

Text of the aside, one or more paragraphs.

---
```

A **Note** is a short question answered on the spot:

```markdown
---

**Note: how many CMB photons are in this room?** At 411 per cubic centimetre, a room of 50 cubic metres holds about $2\times10^{10}$ of them...

---
```

An **In short** gives a new angle on what came before, not a recap:

```markdown
> **In short.** Symmetry does almost all the work. Einstein's field equation is not needed to find the shape of the metric, only to find how $a(t)$ changes with time.
```

When two blocks are next to each other, each keeps both of its rules.

## Accuracy

**Verify every number.** Recompute derived numbers with Python rather than trusting the source or memory.

**Use current values.** Check them against recent primary sources; searching the web for public science is fine. Weave current results into the text where they belong, and say when they date from. Present contested results, such as the Hubble tension, as open, with the competing numbers.

**Link primary sources inline.** Use hyperlinks to the original papers (arXiv abstract page, DOI, ADS) on the claim they support, where reading the paper would help or the claim is surprising. Don't add a reference list. Check that every link opens the paper it names.

**Correct errors in the source, then report them.** If the source has a genuine error (a wrong sign, a misprinted formula, a stale number, a false claim), write the correct version in the notes without comment. After handing over the notes, list each error in the chat: where it is in the source, what it says, and what the correct version is. The reader can then fix their copy of the book.

**Follow the textbook on conventions.** Some differences are choices, not errors: left or right vector spaces, the metric signature, units, sign conventions, notation. Use the textbook's choice, so that the notes and the book read the same way. Where other texts commonly choose differently, say so in a sentence or a short aside: "some texts write scalars on the right; the two conventions describe the same objects". Don't name the textbook. If you don't know which convention the textbook uses, ask before writing.

**Keep notation consistent.** Use one symbol per meaning for the whole document, and define notation where it is first used. Where the field's standard notation clashes, say so where the second meaning first appears. For example, in cosmology η is both conformal time and the baryon-to-photon ratio.

## Standalone

- Never mention the textbook, never cite its author as the source, and never use its chapter, section, theorem, equation, figure, page or exercise numbers. The textbook may change next year, and the notes must not lean on it.
- The notes need no chapter or section numbers of their own. Write headings without numbers ("Polar spaces", not "Chapter 4: Polar spaces" or "4.2 Polar spaces"). Refer to other parts of the notes by topic ("the chapter on dark matter") and link to them.

## Format

Read `references/mkdocs-rendering.md` before writing the first file of a session. It has:

- the user's MkDocs configuration;
- the arithmatex pitfalls, with fixes;
- anchor rules;
- the figure conventions.

The short version:

**Headings.** Use `#` once for the title (`# Maths 4 - Incidence Geometry`; see "The output" above), `##` for chapters, `###` for sections and `####` for subsections. Never go deeper; use a bold lead-in instead. Follow the existing file's heading case. In a new file, use sentence case below the chapter level. Give each section a distinctive heading, since headings are link targets.

**Mathematics on the page.**

- Inline maths goes in `$...$` and display maths in `$$` blocks.
- Put a blank line before every list and table.
- Never put display maths inside a list item.

**Figures.** Add one when a picture shows what words, a table or a text diagram can't. Make it with a saved Python script, from real data where they exist. Number figures continuously through the file and give each a self-contained italic caption. Mention every figure in the text. Mathematics notes benefit from pictures too: draw graphs, configurations, orbit diagrams and plots whenever they help. Small schematics, such as a Buekenhout–Tits diagram, can stay plain text in a fenced code block. Images from the web are allowed when they add something a script can't, such as a rendering or a photograph of a physical model. Download the file, prefer sources that state a licence (Wikimedia Commons first), and end the caption with "Image: author, licence, source URL". The URL is required; give the author and licence when the source states them. The user's notes stay internal, so this attribution is enough. Never use images of the textbook's pages, and search for images with public terms only.

**Python packages.** If a script needs packages from PyPI (matplotlib, sympy, CAMB, MkDocs), install them only into the `.venv` virtual environment in this skill's folder. Create it with `python3 -m venv <skill folder>/.venv` if it doesn't exist, then run scripts with `<skill folder>/.venv/bin/python`. Never install into the system Python or the user's site packages. A venv can break when the skill folder is copied or moved, and the checker rebuilds its own when that happens. If a figure script fails to import a package, reinstall into the venv rather than anywhere else.

**Voice.** Write in a plain, warm, direct voice, saying "we" for the journey through the material. Apply the humanizer skill to the prose. In particular, avoid:

- em dashes;
- inflated words;
- "it's not X, it's Y" constructions;
- lists of three by reflex;
- openers such as "In this section we will explore";
- announcers such as "That is the whole story:" or "that is all it is" (humanizer pattern 26).

**Explain in the order things happen.** Make whoever or whatever acts the subject of the sentence, and tell the steps in the order the reader would carry them out: what we do, then what we get, then what follows. Two habits break this natural expository order. One makes an abstract noun the actor ("another order replaces $A$ by..."), which flips subject and object: the reader, not "another order", is the one reordering. The other tucks the consequence into a trailing clause ("..., with the same eigenvalues"), so the effect arrives squeezed in beside its cause instead of after it. Short sentences are not the goal; the natural order is. Compare:

> Writing $A$ down needs an order for the vertices, but another order replaces $A$ by $P^TAP$ for a permutation matrix $P$, with the same eigenvalues and multiplicities.

> Writing $A$ down needs an order for the vertices. But let's say you changed the order. You would then have $P^TAP$ as the adjacency matrix, where $P$ is a permutation matrix (it changes the order of vertices). This will have the same eigenvalues and multiplicities. These eigenvalues are therefore the eigenvalues of $\Gamma$ itself.

When a sentence feels dense, ask who is doing what, and in what order, then rewrite it in that order.

## Before handing over

1. Run the checker and fix every error:

   ```bash
   python3 <skill folder>/scripts/check_notes.py <notes.md>
   ```

   Add `--anchors` to list every heading's link target. If earlier chapters are in other files (the notes file, or chapters not yet merged into it), add `--earlier <files>` after the notes file: it warns when this chapter defines in bold a term one of them already defines. Read each warning and decide whether it matters.
2. Run the gap checks in `references/gap-checks.md` on the chapter:
   - keep the term ledger up to date;
   - make a purpose table, giving the prerequisites and purpose of every example, result and definition;
   - get a cold read from a fresh reader who has only the background and the text so far;
   - resolve every "defined here but already used" and "already defined in" warning from the checker.
3. Confirm that every number is recomputed or sourced, every link opens the right paper, and every figure matches its caption and the output of its script.
4. Tell the user, briefly:
   - what the chapter covers;
   - what you added beyond the source and what you left out;
   - each error in the source that you corrected: where it is, what the source says, and the correct version;
   - anything that needs their judgement.
