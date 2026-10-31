// Typeset only the maths that arithmatex marked up, using its \( \) and \[ \] delimiters.
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
    processHtmlClass: "arithmatex"
  }
};
