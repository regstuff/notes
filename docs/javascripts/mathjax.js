// Typeset only the maths that arithmatex marked up, using its \( \) and \[ \] delimiters,
// plus the text of table-of-contents and navigation links (md-ellipsis), where a heading's
// maths appears as plain \( \) text because the toc extension drops arithmatex's span.
// If navigation.instant is ever turned on, re-typeset on each page change via document$.
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex|md-ellipsis"
  }
};
