# PFPython

PFPython is an English-first Python practice repository for daily training.

The goal is simple:

- keep every lesson small and runnable
- practice syntax by reading and editing real code
- learn package and module management without extra setup friction
- leave space for your later advanced training
- move from basics to real engineering skills step by step

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

### 2. Core Python

The `core_python/` folder deepens your understanding of how Python really works.

Run these lessons like this:

```bash
python3 core_python/01_scope_and_mutability.py
python3 core_python/04_decorators_intro.py
python3 core_python/06_inheritance_and_polymorphism.py
```

Topics in this stage:

- scope and mutability
- `*args` and `**kwargs`
- higher-order functions
- decorators
- dataclasses
- inheritance and polymorphism
- context managers
- typing and protocols

### 3. Standard Library

The `standard_library/` folder helps you build useful instincts with Python's built-in tools.

Run them like this:

```bash
python3 standard_library/01_datetime_basics.py
python3 standard_library/02_collections_counter.py
python3 standard_library/03_itertools_patterns.py
```

Topics in this stage:

- `datetime`
- `collections`
- `itertools`
- reusable data transformations
- regular expressions
- `sqlite3`
- `csv`

### 4. Engineering

The `engineering/` folder starts moving from syntax drills into small project habits.

Run them like this:

```bash
python3 engineering/01_pytest_basics.py
python3 engineering/02_small_cli_app.py --task "review modules"
python3 engineering/03_config_and_env.py
```

Topics in this stage:

- testing mindset
- CLI design
- configuration patterns
- clearer code organization
- custom exceptions
- mocking basics

### 5. Advanced

The `advanced/` folder introduces ideas you will see in real projects and technical interviews.

Run them like this:

```bash
python3 advanced/01_async_intro.py
python3 advanced/02_custom_iterable.py
python3 advanced/03_simple_profiling.py
```

Topics in this stage:

- async programming
- custom iterables
- simple profiling and measurement
- generator pipelines
- descriptors

### 6. Projects

The `projects/` folder turns lessons into small runnable applications.

Run them like this:

```bash
python3 projects/01_todo_cli.py --add "review generators"
python3 projects/02_file_organizer_preview.py
python3 projects/03_study_tracker_sqlite.py
```

Use these projects to practice:

- splitting logic into helper functions
- persistent data with files or databases
- command-line workflows
- refactoring from a single file into multiple modules later

### 7. Tests

The `tests/` folder introduces real test-style files while still allowing direct execution.

Run them like this:

```bash
python3 tests/test_pfpython_models.py
python3 tests/test_pfpython_practice.py
```

Later, when `pytest` is available, you can also run:

```bash
pytest
```

### 8. Modules

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

### 9. Package Practice

The `pfpython/` package contains reusable helpers and simple models.

Try these commands:

```bash
python3 -m pfpython
python3 -m pfpython.practice
python3 pfpython/banner.py
python3 pfpython/practice.py
```

### 10. How To Practice

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
  core_python/        # deeper Python language concepts
  standard_library/   # practical official-library practice
  engineering/        # testing, CLI, config, and project habits
  advanced/           # async, profiling, and harder abstractions
  projects/           # small runnable applications
  tests/              # direct-run tests and later pytest practice
  modules/            # imports, packages, CLI, and data flow
  pfpython/           # reusable package modules
  data/               # tiny practice data files
  tools/              # helper scripts for repository checks
  pyproject.toml      # basic project metadata
```

## Commands You Will Use Often

```bash
python3 foundations/06_functions.py
python3 core_python/05_dataclasses.py
python3 standard_library/02_collections_counter.py
python3 engineering/02_small_cli_app.py --task Learner
python3 advanced/01_async_intro.py
python3 projects/01_todo_cli.py --add "finish one lesson"
python3 tests/test_pfpython_models.py
python3 modules/03_cli_arguments.py --name Learner
python3 -m pfpython
python3 tools/run_everything.py
PYTHONPYCACHEPREFIX=.pycache python3 -m compileall .
```

## Training Rules For Yourself

- keep examples small
- prefer clear names over clever code
- write one idea per lesson
- when confused, print values and types
- revisit old lessons and refactor them
- build tiny utilities before building larger apps
- test one idea at a time
- revisit projects and split them into modules as you improve

## Next Expansion Ideas

- HTTP requests
- decorators in larger designs
- file parsers
- logging patterns
- thread pools and process pools
- real pytest fixtures
- packaging and publishing
- multi-file projects with internal packages

Build slowly, stay curious, and use this repo as your personal Python gym.
