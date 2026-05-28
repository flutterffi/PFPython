# PFPython

PFPython is an English-first Python practice repository for daily training.

The goal is simple:

- keep every lesson small and runnable
- practice syntax by reading and editing real code
- learn package and module management without extra setup friction
- leave space for your later advanced training

## Learning Path

### 1. Foundations

Each file in `foundations/` is a standalone lesson.

Run a lesson like this:

```bash
python3 foundations/01_hello_world.py
```

Suggested order:

1. `01_hello_world.py`
2. `02_variables_and_types.py`
3. `03_strings_and_numbers.py`
4. `04_conditionals.py`
5. `05_loops.py`
6. `06_functions.py`
7. `07_collections.py`
8. `08_comprehensions.py`
9. `09_classes.py`
10. `10_exceptions.py`
11. `11_files_and_paths.py`
12. `12_iterators_and_generators.py`

### 2. Modules

The `modules/` folder helps you practice imports, packages, command-line arguments, and basic project structure.

Run them like this:

```bash
python3 modules/01_imports_and_helpers.py
python3 modules/02_package_usage.py
python3 modules/03_cli_arguments.py --name Plato
python3 modules/04_json_workflow.py
```

These examples are meant to help you practice:

- `import` and `from ... import ...`
- `if __name__ == "__main__"`
- package layout
- `python -m`
- `pathlib`
- simple data loading with `json`

### 3. Package Practice

The `pfpython/` package contains reusable helpers and simple models.

Try these commands:

```bash
python3 -m pfpython
python3 -m pfpython.practice
python3 pfpython/banner.py
python3 pfpython/practice.py
```

### 4. How To Practice

Use the repository in loops:

1. Run a lesson.
2. Predict the output before reading it.
3. Change one rule or value.
4. Run it again.
5. Add your own variation beside it later.

Good modifications to try:

- change a `for` loop into a `while` loop
- add your own helper function and import it
- turn printed text into returned values
- create a new class with one method
- raise your own custom exception
- add a new module and wire it into the package

## Repository Layout

```text
PFPython/
  foundations/        # syntax drills, one runnable file per lesson
  modules/            # imports, packages, CLI, and data flow
  pfpython/           # reusable package modules
  data/               # tiny practice data files
  tools/              # helper scripts for repository checks
  pyproject.toml      # basic project metadata
```

## Commands You Will Use Often

```bash
python3 foundations/06_functions.py
python3 modules/03_cli_arguments.py --name Learner
python3 -m pfpython
python3 tools/run_everything.py
python3 -m compileall .
```

## Training Rules For Yourself

- keep examples small
- prefer clear names over clever code
- write one idea per lesson
- when confused, print values and types
- revisit old lessons and refactor them

## Next Expansion Ideas

- decorators
- dataclasses
- context managers
- regular expressions
- unit tests with `pytest`
- async programming
- HTTP requests
- typing and protocols
- packaging and publishing

Build slowly, stay curious, and use this repo as your personal Python gym.
