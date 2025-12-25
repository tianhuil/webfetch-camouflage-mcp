# Rules for python repos

## General

- Use `uv` for package manager.

## Coding Style

- Prefer to write functional code. Prefer list comprehensions for map, flatmap, and filter: `[func(x) for x in xs if condition(x)]`.
- Prefer to not mutate variables, even though Python allows mutation (pretend variables are all using typescript `const` not `let`).
- Explicitly type where practicable using pyright. Look at the libraries and import and use those types; do not make up types.
- Always avoid using type `Any` type.
- Add docstring to every class and function.
- Place `try`/`except` only at the root calling function. Do not place `try`/`except` in each intermediate or leaf function.
- If a library is missing a pyright type (e.g. `requests`), add the types as a development dependency (e.g. `types-requests`).
- For a multiline string, use `textwrap.dedent` and format nicely.

## Validation

Whenever you make a change, run `ruff` and `pyright` to confirm tests pass.
Use `git diff` and review code changes for following the rules under "Coding Style" section.
