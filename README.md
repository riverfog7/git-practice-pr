# git-practice-pr

![tests](https://github.com/riverfog7/git-practice-pr/actions/workflows/tests.yml/badge.svg)

# Git PR Practice

Practice the GitHub pull request workflow by adding a small Python function.

## Goal

Open a pull request that adds your own submission file. Your function should print and return your name plus the input string.

## Setup

Install dependencies:

```bash
uv sync --dev
```

Run tests:

```bash
uv run pytest
```

Install pre-commit hooks:

```bash
uv run pre-commit install
```

Run all pre-commit checks manually:

```bash
uv run pre-commit run --all-files
```

## Instructions

1. Create a new branch.
2. Add a file named `src/git_practice/submissions/<your_name>.py`.
3. Replace `<your_name>` with your GitHub username.
4. Define `NAME` and `print_message` in your file.
5. Run `uv run pytest`.
6. Open a pull request.

## Example

If your GitHub username is `riverfog7`, create this file:

`src/git_practice/submissions/riverfog7.py`

```python
NAME = "riverfog7"


def print_message(input_str: str) -> str:
    message = f"{NAME}: {input_str}"
    print(message)
    return message
```

The test expects `print_message("hello")` to print and return:

```text
riverfog7: hello
```

The filename and `NAME` value must match exactly.

## CI

GitHub Actions runs pre-commit checks and `uv run pytest` for every pull request and every push to `main`.
