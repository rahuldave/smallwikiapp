# wikiapp: every task is a recipe here. `just` lists them; `just help VERB` explains one.

# Each word after a recipe's name reaches its commands whole, as "$1", "$2" and so on; "$@" is all of them
set positional-arguments

[private]
default:
    @just --list --unsorted

# Explain a verb: the comment above its recipe, then the recipe. Alone, the list
[no-exit-message]
help *verb:
    #!/usr/bin/env sh
    if [ "$#" -eq 0 ]; then just --list --unsorted; exit 0; fi
    shown=$(just --show "$1") || exit 1
    printf '%s\n' "$shown"

# Install Python and every dependency into .venv, exactly as the lockfile says
[group('setup')]
setup *args:
    @{{ if args == "help" { "just help setup" } else { "uv sync --locked" } }}

# Run the tests. Extra arguments go to pytest: just test -k title
[group('quality')]
[no-exit-message]
test *args:
    {{ if args == "help" { "just help test" } else { 'uv run pytest "$@"' } }}

# Format the code, one way. Extra arguments go to ruff: just fmt --check, just fmt --diff
[group('quality')]
[no-exit-message]
fmt *args:
    {{ if args == "help" { "just help fmt" } else { 'uv run ruff format "$@"' } }}

# Check the code against the rules in pyproject.toml. Extra arguments go to ruff: just lint --fix
[group('quality')]
[no-exit-message]
lint *args:
    {{ if args == "help" { "just help lint" } else { 'uv run ruff check "$@"' } }}
