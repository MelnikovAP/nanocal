# Code Style Guide

### Main rules:
- Don't use tab `\t` as a separator. Use four spaces instead.
- Comments should be necessary to explain some logic and only in English.
- Class names should use `CamelCase` convention.
- Function names should use `snake_case` convention.
- Add an empty line at the end of each file.
- Get rid of `import` statements of unused modules and packages.
- A single `#` symbol following by a single space `" "` for comments.
- Two spaces before `#` to add comments in the same line of code.
- No more than 120 symbols in the same line of code.
- Use `"` for strings with more than one symbols, and `'` for a single-symbol strings.
- Add space before and after operators (`=, ==, >, <` etc.).
- Use `_` as a prefix of protected and private class fields.
- Use a `@staticmethod` decorator for class methods that don't require `self`.
- Initialize containers like this: `l = list(), d = dict(), s = set()`.
- 

### Best resources:
1. https://google.github.io/styleguide/pyguide.html
2. https://peps.python.org/pep-0008/