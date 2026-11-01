# Gap checks: will the reader get stuck?

A gap is any point where the reader, with only their background and the notes so far, cannot follow. Run these checks twice:

- on the content plan, before showing it to the user;
- on each chapter of notes, before handing it over.

The user found every kind of gap below in a plan that looked complete. They are easy to miss from the inside, because the writer already knows every term.

## The kinds of gap

1. **A name before its object.** A named object (a particular graph, design, group, polygon or space) is used before the notes have built it. The name alone tells the reader nothing.

   *Example:* "the Petersen spectrum", in a section that never said what the Petersen graph is.

   *Fix:* build the object where it first appears (a construction, plus a picture or a small table), or don't name it there.
2. **Jargon.** A word with a technical meaning that the reader hasn't been given. This includes words from other fields used in asides.

   *Example:* "spectrum" for the list of eigenvalues of a matrix; "tight-binding" or "Mermin–Peres" in an aside.

   *Fix:* define it in a line, or use plain words.
3. **A hook that needs later machinery.** An opening that only makes sense after the chapter has been read.

   *Example:* "this quadrangle needs a 72/5-dimensional eigenspace", before the notes have shown how a geometry leads to a matrix.

   *Fix:* pose the puzzle in terms the reader already has, and deliver the explanation where the machinery arrives.
4. **An unstated prerequisite.** A concept used as if known, with no record of where it was introduced.

   *Example:* "geodesic" in a chapter on polygons; "t-design and s-design" in a chapter on designs.

   *Fix:* every term is either in the reader's background (say which part) or introduced earlier in the notes. On reuse, link back to where it was introduced.
5. **A unit without a purpose.** An example, result, definition, proof idea, aside or table whose purpose isn't stated. "The book uses it later" is not a purpose. For each kind, say:
   - for an example: what the reader should notice. For instance, "a graph where every vertex has 3 neighbours and any two vertices are at most 2 steps apart has at most 10 vertices; reaching 10 forces a rigid structure; local rules force global facts";
   - for a result: what question it answers, what it is used for later, and what each hypothesis does (what breaks without it);
   - for a definition: why it has its shape, and where it is used;
   - for a proof idea: the one step that makes it work;
   - for an aside: its link to the reader's background;
   - for a table or figure: what to look at in it.

   If a definition or result is never used again in the selection, give it one line or drop it.
6. **Ideas out of order.** An example comes before the definitions it relies on. A plan line that lists terms and examples together ("valency, girth, diameter, on C₆, Petersen and the cube") hides the order.

   *Fix:* write each subsection as a sequence: idea, idea, example (with its lesson), and so on.
7. **Material moved earlier than the source.** The notes use something before the textbook introduces it, for example to have a running example.

   *Fix:* that is fine, but the notes must then construct it fully at that earlier point. The textbook's own definition comes later and can't be relied on.
8. **A tool far from its payoff.** Machinery built chapters before it is used (for example, distance-regular graph theory that only pays off in the Feit–Higman theorem).

   *Fix:* state the destination when the tool is built, and link back to it at the payoff.
9. **A long argument with no map.** A proof or derivation over several steps, with nothing saying where it is going.

   *Fix:* give the steps in a few lines first, then do them.
10. **Notation problems.** Three kinds to look for:
    - a symbol never read aloud;
    - one letter with several meanings across the notes (λ as a graph parameter, a design parameter and a scalar);
    - notation that differs from the textbook's or from the reader's earlier notes.

    *Fix:* say how to read each symbol once; flag a reused letter at its second meaning; give other common notation alongside ("also written ..."), without mentioning the textbook.
11. **Words that differ from the textbook.** The reader reads the book next, so a synonym the book never uses ("spectrum" for the book's "eigenvalues", a nickname for a named geometry) will confuse them there.

    *Fix:* give the book's word alongside as a synonym ("the valency, also called the degree"), without mentioning the book: the notes still never refer to the textbook.
12. **Too much at once.** More than two or three new terms in one subsection.

    *Fix:* split the subsection, or drop the terms that are never used again.
13. **No sense of size.** An abstract object with no counts and no smallest case.

    *Fix:* give the smallest case and its numbers.
14. **No picture.** An object the reader has to hold in mind, with no figure or text diagram.
15. **A promise not kept.** "We will see later..." with no matching delivery in the notes, for example because the proof sits in a section the user didn't select.

    *Fix:* say so, or give the idea in a few lines.
16. **An unexplained generality.** Conventions that look pedantic, such as allowing thin lines or repeated lines.

    *Fix:* say why the textbook keeps them.
17. **A hard passage in the textbook.** A step the book skips or compresses, which the reader will meet right after the notes.

    *Fix:* give the idea beforehand, citing the page in the plan (never in the notes).
18. **A running example with many names.** The same object appears under several descriptions (as a polar space, a graph with given parameters, a quadrangle).

    *Fix:* add a small "who's who" table at its first appearance, and link back to it at each reuse.

## How to run the checks

**Term ledger.** Walk through the plan or the notes in order. For every term, name, object or result, record one of:

- KNOWN: in the reader's background, saying which course or which earlier set of notes;
- INTRODUCED: at a named earlier point in these notes;
- GAP: neither.

Search the reader's earlier notes rather than guessing: start from `check_notes.py --terms` on the notes file and on any earlier chapters not yet merged into it. Keep the ledger while writing, so later chapters can check against it.

**Purpose table.** For every example, result, definition, opening, transition, proof idea, aside and table, record three things:
- its prerequisites, with where each is defined;
- its purpose (the lesson, what question it answers, or its payoff);
- for a result, what its hypotheses do.

Flag anything with an undefined prerequisite, no clear purpose, or an ordering conflict. Then go through kinds 8-18 above.

**Cold read.** Give a fresh reader the background list and the text so far, and nothing else. The writer's own context hides gaps. That reader can be a new subagent, or another agent such as Gemini or Codex through the cowork skill. Ask it to list:

- every term it would not know at that point;
- every example whose purpose is unclear;
- every hook or motivation that refers to something not yet explained.

If no fresh reader is available, read the text yourself as the reader would, one paragraph at a time.

**The checker.** `scripts/check_notes.py` warns when a term the notes define in **bold** already appears in the prose above its definition. Bold a term only where it is defined. For each warning, do one of three things:

- define the term at its first use;
- turn the first use into a link to where it is defined;
- reword the first use so it no longer needs the term.

A mention inside a link is treated as a deliberate forward reference: once a term has been mentioned in a link, its later mentions aren't flagged either.

When you review a warning and the use is fine, add the term to a hidden comment anywhere in the file: `<!-- terms checked: term one; term two -->`. A use is fine when it is glossed in place, known from the background, or a false alarm such as an ordinary word. The comment doesn't render on the site, and the next run stays quiet.

With `--earlier` and the files of earlier chapters, the checker also warns when this chapter defines in bold a term that one of them already defines in bold. Link back to the earlier definition instead, with a reminder if it was far back. If the restatement is deliberate, for example because the term now means something more general, say so in the text and list the term in the same `terms checked` comment.

## What the plan must show

The plan is for the user to judge, so it must be readable by the user.

- Name each object with a few words of explanation the first time it appears ("the Petersen graph: pairs from {1,…,5}, joined when disjoint").
- Write each subsection's line as an ordered sequence. Give every example its lesson, and every result and definition its purpose.
- Note where each prerequisite comes from when it isn't obvious: "geodesic: defined in the first section"; "eigenspaces: core linear algebra".
