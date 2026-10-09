# smallwikiapp

`wikiapp` is the command this project builds, step by step. By the last step it prints the title and the summary
of a random Wikipedia page, in a language you choose.

The command is small on purpose. The history of this repository shows how to build the project around it,
one step at a time:

- packages and dependencies, with uv
- tests
- a library split from the app
- format, lint and types
- CI, and documentation made from the code

It is a rebuild of [wikiapp](https://github.com/rahuldave/wikiapp), which follows Claudio Jolowicz's
[Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/) series, with
[uv](https://docs.astral.sh/uv/) and [just](https://just.systems/) in place of pixi.

## What you need

| Tool | What it is for |
|---|---|
| [uv](https://docs.astral.sh/uv/) | Python itself, the dependencies, and running the command |
| [just](https://just.systems/) | The project's tasks. `just` lists them |

Then `just setup`, and `uv run wikiapp`.

## What is here

| Path | What it is |
|---|---|
| `pyproject.toml`, `uv.lock` | The project: its name, its Python, its dependencies, and the exact versions installed |
| `src/wikiapp/` | The app. `console.py` is the `wikiapp` command |
| `packages/wikirandom/` | The library the app uses: a random page of Wikipedia. A package of its own |
| `tests/` | The tests. `just test` runs them |
| `docs/` | The docs site. smalldocs makes its reference from the code |
| `justfile` | Every task of the project, one recipe each. `just help VERB` explains one |
| `.python-version` | The Python version the project uses |
| `.gitignore` | Everything a run makes, ignored from the first commit on |
| `LICENSE` | The licence, Apache-2.0 |

## How the history is organised

The history has steps. Each step is a tag, `step-00`, `step-01` and so on, and the message of the tag
says what the step adds. The commits between two tags are the *moves*. A move is a small commit that does
one action, and its subject starts `step-NN.k:`. The last move of a step is the tagged commit, and its
subject starts `step-NN:`. The message of each commit says what the commit does and why.

```
git tag -n3 --list 'step-*'           # the steps, and what each adds
git log --oneline --reverse           # every move, in order
git switch --detach step-01           # the project as it was at a step
```

The walk through these steps, with its notes and slides, is in
[smallwikiapp-walk](https://github.com/rahuldave/smallwikiapp-walk).

## Licence

Apache-2.0: see [`LICENSE`](LICENSE).
