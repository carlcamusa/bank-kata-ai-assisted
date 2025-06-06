# Bank Kata - An AI-Assisted TDD Journey

This repository contains a Python implementation of the classic Bank Kata programming exercise. The primary goal of this project was to explore the capabilities of AI-assisted development.

## AI-Driven Development

The entirety of the code in this project was generated through a pair-programming session with Gemini 2.5 Pro, an AI coding assistant operating within the Cursor IDE.

The development process was heavily influenced by a specific set of rules and principles provided to the AI (see `/.cursorrules` in this repository). These rules enforced:

-   **Test-Driven Development (TDD):** Always writing a failing test before any implementation.
-   **Incremental "Baby Steps":** Making small, manageable changes one at a time.
-   **Simplicity:** Adhering to the simplest possible solution.
-   **Clean Code:** Creating small, single-responsibility methods and meaningful names.

This structured approach, guided by the AI and the predefined rules, had a significant impact on the final code quality, its structure, and test coverage.

## Development Journey

The project was developed iteratively, following a strict TDD cycle. The history of the conversation with the AI that produced the code can be found in the `.specstory/history` directory. The key stages were:

1.  **Initial Test Setup:** The process began by establishing the foundational test structure, creating the first failing test case that drove the initial implementation.
2.  **Core Feature Implementation:** The main functionality—printing a formatted bank account statement—was developed. This involved creating the initial classes for transactions, accounts, and the statement printer.
3.  **Refactoring with a First-Class Collection:** To improve the design and better encapsulate behavior, the simple list of transactions was refactored into a `TransactionLedger` class. This is an example of applying the "First-Class Collection" pattern to centralize transaction management logic.
4.  **Expanding Unit Test Coverage:** Additional unit tests were implemented to cover more scenarios and edge cases, ensuring the robustness and correctness of the application after refactoring.

## Initial Resources

The original problem description and requirements for the Bank Kata that were used as the starting point for this project can be found in the `resources` folder.

## Python Boilerplate ![status](https://github.com/pmareke/python-boilerplate/actions/workflows/app.yml/badge.svg)

- This repository is meant to be used as a fast starter point.
- The Python version is the 3.12.
- The project has configured a [Github Action](https://github.com/pmareke/python-boilerplate/actions) which runs on every push to the `main` branch.

## Requirements

- You only need to have [uv](https://docs.astral.sh/uv) installed.

## Folder structure

- There is a `tests` folder with the tests files.
  - In order to add new tests please follow the [pytest](https://docs.pytest.org/en/7.1.x/getting-started.html) recommendations.
- The production code goes inside the `src` folder.
- Inside the `scripts` folder you can find the git hooks files.

## Project commands

The project uses [Makefiles](https://www.gnu.org/software/make/manual/html_node/Introduction.html) to run the most common tasks:

- `add-package package=XXX`: Installs the package XXX in the app, ex: `make install package=requests`.
- `build`: Builds the app.
- `check-format`: Checks the code format.
- `check-lint`: Checks the code style.
- `check-typing`: Runs a static analyzer over the code in order to find issues.
- `format`: Formats the code.
- `lint`: Lints the code.
- `help` : Shows this help.
- `install`: Installs the app packages.
- `local-setup`: Sets up the local environment (e.g. install git hooks).
- `run`: Runs the app.
- `test`: Run all the tests.
- `update`: Updates the app packages.
- `watch`: Run all the tests in watch mode.

**Important: Please run the `make local-setup` command before starting with the code.**

_In order to create a commit you have to pass the pre-commit phase which runs the check and test commands._

## Packages

This project uses [uv](https://docs.astral.sh/uv) as the package manager.

### Testing

- [pytest](https://docs.pytest.org/en/7.1.x/contents.html): Testing runner.
- [doublex](https://github.com/davidvilla/python-doublex): Powerful test doubles framework for Python.
- [expects](https://expects.readthedocs.io/en/stable/): An expressive and extensible TDD/BDD assertion library for Python..
- [doublex-expects](https://github.com/jaimegildesagredo/doublex-expects): A matchers library for the Expects assertion librar.

### Code style

- [ty](https://github.com/astral-sh/ty): A static type checker.
- [ruff](https://github.com/astral-sh/ruff): An extremely fast Python linter, written in Rust..

## Contributors

Special thanks to:
- [GoldraK](https://github.com/GoldraK).
- [Alex Lopez](https://github.com/alexlopezc)
