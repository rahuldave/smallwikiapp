# smallwikiapp

`wikiapp` is a command that prints the title and the summary of a random Wikipedia page, in a language you
choose:

```
$ uv run wikiapp --language fr
Aiguille de Borderan
L'aiguille de Borderan est un sommet de la chaîne des Aravis qui
culmine à 2 492 m d'altitude, entre les départements de la Savoie et
de la Haute-Savoie.
```

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
| `.pre-commit-config.yaml` | The git hook: `just check` before every commit. `just hook` installs it |
| `.github/workflows/test.yaml` | What GitHub runs on every push to main and every pull request |
| `.github/workflows/docs.yaml` | On every push to main, GitHub builds the docs site and publishes it at https://rahuldave.com/smallwikiapp/ |
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

<!-- steps:start -->
- **[step-00](https://github.com/rahuldave/smallwikiapp/tree/step-00) The project.** A uv project whose command prints one line, and a justfile with `setup` and `help`. `just setup` makes `.venv` exactly as `uv.lock` says.
- **[step-01](https://github.com/rahuldave/smallwikiapp/tree/step-01) A random page.** The command asks Wikipedia for a random page and prints it. Wikipedia wants a User-Agent first.
  - [`step-01.1`](https://github.com/rahuldave/smallwikiapp/commit/36d49582843a575d84ed178ad66157913be4c59c) click and requests, the two dependencies
  - [`step-01.2`](https://github.com/rahuldave/smallwikiapp/commit/571c82ebd31fee095e56a45cf2bf77eb7bfe0c8c) main asks Wikipedia for a random page, and is refused
  - [`step-01.3`](https://github.com/rahuldave/smallwikiapp/commit/0ffd5df563acb876953855d86be30b6952ecfd44) a User-Agent, and Wikipedia answers
  - [`step-01.4`](https://github.com/rahuldave/smallwikiapp/commit/f05d3c31be2cf640cc2aa4345658b8eebc394d60) a random page, and --version
- **[step-02](https://github.com/rahuldave/smallwikiapp/tree/step-02) Tests, with mocks.** A test that runs the command, and a mock in place of Wikipedia so that the other tests need no network. Coverage on every run.
  - [`step-02.1`](https://github.com/rahuldave/smallwikiapp/commit/46dc20fb9092170695699eaa052f4830563cb930) uv installs every dependency group
  - [`step-02.2`](https://github.com/rahuldave/smallwikiapp/commit/6d7a6cfdae6008a9687f3525348ab24ea05930cc) the first test
  - [`step-02.3`](https://github.com/rahuldave/smallwikiapp/commit/d92e2dec921d6322e2a356af20dafef3837c1849) pytest, in the group test
  - [`step-02.4`](https://github.com/rahuldave/smallwikiapp/commit/45807a0ddd9f97798c3f86a82b19782d4df45837) just test
  - [`step-02.5`](https://github.com/rahuldave/smallwikiapp/commit/8435ae56cf5630c401d83760b4dffe1fe5bde109) the runner as a fixture
  - [`step-02.6`](https://github.com/rahuldave/smallwikiapp/commit/55b7b55dffa30e6eb91a88c882201f955271e28d) pytest-mock, in the group test
  - [`step-02.7`](https://github.com/rahuldave/smallwikiapp/commit/7c1911b9f0155df43da70d010b25fc1ec947fe7c) a mock in place of Wikipedia
  - [`step-02.8`](https://github.com/rahuldave/smallwikiapp/commit/9be013d11b88d0e40680024a8ea99d501c681252) tests that the request is made, to the right address
  - [`step-02.9`](https://github.com/rahuldave/smallwikiapp/commit/bfc38e738984492a5dbf6a1a6a0b6691baad4c34) a test of a failed request
  - [`step-02.10`](https://github.com/rahuldave/smallwikiapp/commit/8409e0f2e7f68a697de1e8bf32a745658364f17f) pytest-cov, in the group test
  - [`step-02.11`](https://github.com/rahuldave/smallwikiapp/commit/7508f1d424d5f906ee4630be09b2fddf3483e9c4) coverage, on every run
- **[step-03](https://github.com/rahuldave/smallwikiapp/tree/step-03) A library and an app.** wikipedia.py talks to Wikipedia, in any language, and raises its own error. console.py is the command that uses it.
  - [`step-03.1`](https://github.com/rahuldave/smallwikiapp/commit/3f6d8cf59ab3fd59dc157e169a7c79aeb13aa205) the request moves into random_page, in wikipedia.py
  - [`step-03.2`](https://github.com/rahuldave/smallwikiapp/commit/a65f7f11432be0a56de38e7d4babe10bda735c2c) the mock moves to conftest.py, for every test file
  - [`step-03.3`](https://github.com/rahuldave/smallwikiapp/commit/d9d02ca26fd3c3633e5ce22b18ecb2198e28a520) random_page takes a language
  - [`step-03.4`](https://github.com/rahuldave/smallwikiapp/commit/5705a559523968eeab5379a65e30bf4122ba578e) wikiapp --language
  - [`step-03.5`](https://github.com/rahuldave/smallwikiapp/commit/a6f5ae9a475d916d4053315c9e6699f16951193f) wikipedia.py raises its own error, WikipediaError
  - [`step-03.6`](https://github.com/rahuldave/smallwikiapp/commit/b6942869d5fcfffff81beb598630288fe3a67372) the command turns WikipediaError into a message
- **[step-04](https://github.com/rahuldave/smallwikiapp/tree/step-04) Format, lint, a hook.** ruff formats the code and finds five problems, one of them a request with no timeout. `just check` runs every check, and a git hook runs it before each commit.
  - [`step-04.1`](https://github.com/rahuldave/smallwikiapp/commit/8f7b800001ee35d8db80c47521b02777047c019d) ruff, in the group lint
  - [`step-04.2`](https://github.com/rahuldave/smallwikiapp/commit/31445743379186b800fd4c035c8f04eed7ad7f3d) the settings of ruff, and just fmt
  - [`step-04.3`](https://github.com/rahuldave/smallwikiapp/commit/6690eee9f7e177a6df2ea5e1821b8f581948bc85) the code, formatted
  - [`step-04.4`](https://github.com/rahuldave/smallwikiapp/commit/589f2f691557470eac084858d430a302c98390ce) the linter's rules, and just lint
  - [`step-04.5`](https://github.com/rahuldave/smallwikiapp/commit/2ec7932b37e21c1533f319c03e0533bc755f6da7) the tests' imports at the top, and no unused variables
  - [`step-04.6`](https://github.com/rahuldave/smallwikiapp/commit/0fb4985582732edf7372a4b90659d703db138446) a timeout of 10 seconds
  - [`step-04.7`](https://github.com/rahuldave/smallwikiapp/commit/a57134d1cef6ff24803235ace966e5870046fbd9) just lint --fix sorts the imports
  - [`step-04.8`](https://github.com/rahuldave/smallwikiapp/commit/4e710d50a22967ebff9502eacbdada54313ebe70) validate-pyproject, in the group lint
  - [`step-04.9`](https://github.com/rahuldave/smallwikiapp/commit/d8a9c8f71eb58893025360c20b32c9078e5b0c3c) just lint-config, the check of the configuration
  - [`step-04.10`](https://github.com/rahuldave/smallwikiapp/commit/b7469ee81a824a46e6799d60957ea09d7cf2eade) a locked lockfile, with UV_LOCKED
  - [`step-04.11`](https://github.com/rahuldave/smallwikiapp/commit/1f73d6af30cce37adbe58a2ebfd6e80c00e4c543) just check, everything a commit must pass
  - [`step-04.12`](https://github.com/rahuldave/smallwikiapp/commit/29291b3575f2efd8f6062e3d04bbea648ae1fc11) pre-commit, in the group lint
  - [`step-04.13`](https://github.com/rahuldave/smallwikiapp/commit/6860da13f0fdf9595f32390f2fa70fe0976159b1) a git hook that runs just check
- **[step-05](https://github.com/rahuldave/smallwikiapp/tree/step-05) Types.** ty checks the types and finds a call that asks for a version with a name that can be None. Every parameter and return gets a type, and `just check` runs ty.
  - [`step-05.1`](https://github.com/rahuldave/smallwikiapp/commit/56a11f0bb31a607e6c5ff37454c7915f2eddd86d) ty, in the group lint
  - [`step-05.2`](https://github.com/rahuldave/smallwikiapp/commit/2a5904d01d950678e8364d7f6958dccaf5b69368) just types
  - [`step-05.3`](https://github.com/rahuldave/smallwikiapp/commit/b7a3e6d212b439920f62f0a023554b86d14ebd4e) the version of "wikiapp", by name
  - [`step-05.4`](https://github.com/rahuldave/smallwikiapp/commit/06613b9b25a8f16c7e60cf52803b2e471161d854) the linter asks for a type on every parameter and return
  - [`step-05.5`](https://github.com/rahuldave/smallwikiapp/commit/643f65323fd11c5c6f518c59431b13867e155952) types in the code
  - [`step-05.6`](https://github.com/rahuldave/smallwikiapp/commit/5873353449adaf1734a9cb14d13262486b1fb5d5) types in the tests
  - [`step-05.7`](https://github.com/rahuldave/smallwikiapp/commit/701783af434e19b17e38a10898a39adc1dc5dae9) types join just check
- **[step-06](https://github.com/rahuldave/smallwikiapp/tree/step-06) End to end, and CI.** The tests that need the network run only when asked for. GitHub runs the others on three systems and four Pythons.
  - [`step-06.1`](https://github.com/rahuldave/smallwikiapp/commit/35f4ffc8c67a55ff91a9e7ec02c6de3b90179735) the test that asks Wikipedia runs only when asked for
  - [`step-06.2`](https://github.com/rahuldave/smallwikiapp/commit/307d4d7b36bb9dc7bc8ad601c8275d5241283e35) an end-to-end test of the library
  - [`step-06.3`](https://github.com/rahuldave/smallwikiapp/commit/b97ee4cfc59182c79e4a09ca19a7790b25f25264) any Python from 3.11 on
  - [`step-06.4`](https://github.com/rahuldave/smallwikiapp/commit/d8af75e8fd576ae8d09cb76ed960b1c4892e0a84) the lockfile, for every Python from 3.11 on
  - [`step-06.5`](https://github.com/rahuldave/smallwikiapp/commit/20cf458261edc55b725da39a99c9b37ef5d24657) GitHub runs the tests on three systems and four Pythons
- **[step-07](https://github.com/rahuldave/smallwikiapp/tree/step-07) A page with a shape.** A pydantic model says that a page has a title and an extract. An answer without them is an error, like a failed request. A language that is not a language code is an error too.
  - [`step-07.1`](https://github.com/rahuldave/smallwikiapp/commit/47fc24f56c9129f7c17f1c26092a6cfaffa3bf10) pydantic
  - [`step-07.2`](https://github.com/rahuldave/smallwikiapp/commit/1baf0602c1d1cec79277c2faec438b76a9a8c768) a Page with a title and an extract
  - [`step-07.3`](https://github.com/rahuldave/smallwikiapp/commit/88fe0e20d645b581ff1e3ab4bb9679978bc3d38d) random_page returns a Page
  - [`step-07.4`](https://github.com/rahuldave/smallwikiapp/commit/06ff2caa1958318b960fa9b9c84b32b3a23ae18d) an answer that is not a page is a WikipediaError too
  - [`step-07.5`](https://github.com/rahuldave/smallwikiapp/commit/be473b80441f82ce87bf800deeb432fd4212dea4) the language is checked before it goes into the address
- **[step-08](https://github.com/rahuldave/smallwikiapp/tree/step-08) Docs from the code.** Every function says what it does and what each parameter is, beside the code. smalldocs makes the reference pages from the code, and `just check` checks the docs.
  - [`step-08.1`](https://github.com/rahuldave/smallwikiapp/commit/71726f393670206ea480aaa2edc03ddeeeebc1fe) smalldocs, in the group docs
  - [`step-08.2`](https://github.com/rahuldave/smallwikiapp/commit/40d4293f5902e4a5ee51c9240e0eab4b59de797f) what is not documented
  - [`step-08.3`](https://github.com/rahuldave/smallwikiapp/commit/66a702fe4a01d424177085b9ef056dd8d8d11cc8) the library documented
  - [`step-08.4`](https://github.com/rahuldave/smallwikiapp/commit/bb648b91f4aba037eac04caa5cd7b41095e7c388) the command documented
  - [`step-08.5`](https://github.com/rahuldave/smallwikiapp/commit/7a0e5094887304538655b706752de99408df2d97) the tests documented
  - [`step-08.6`](https://github.com/rahuldave/smallwikiapp/commit/e99ed4f3ab32aec60ae0e2329f4779673a5955d0) a docs site, built from the code by smalldocs
  - [`step-08.7`](https://github.com/rahuldave/smallwikiapp/commit/79c80120fc8fc12ec7b38474294b422e86619362) the README names the tests and the docs
  - [`step-08.8`](https://github.com/rahuldave/smallwikiapp/commit/ce0734f1272cf16f4aadeaa6712e589010ccd69f) the docs check joins just check
- **[step-08b](https://github.com/rahuldave/smallwikiapp/tree/step-08b) The docs on GitHub Pages.** GitHub builds the docs site on every push to main, and publishes it. Each job on GitHub installs only the group it needs. The tests install the group test, and the site the group docs.
  - [`step-08b.1`](https://github.com/rahuldave/smallwikiapp/commit/971e9d780fd539d13f49af3fbb00c1145fd22aa0) on GitHub, the job tests installs only the group test
  - [`step-08b.2`](https://github.com/rahuldave/smallwikiapp/commit/39a4b09f85638bbe8424b243c4ba4477070f2740) GitHub publishes the docs site
- **[step-09](https://github.com/rahuldave/smallwikiapp/tree/step-09) The library as a package.** wikirandom, the code that asks Wikipedia, is a package of its own in the same repository, a uv workspace. The app depends on it.
  - [`step-09.1`](https://github.com/rahuldave/smallwikiapp/commit/01364831243e6c4c4f2fab3756eb1c633f6903c8) an empty library, wikirandom, in the workspace
  - [`step-09.2`](https://github.com/rahuldave/smallwikiapp/commit/c153cdfc43300110bd63502b3d53a85ab3aa79f1) requests and pydantic, for the library
  - [`step-09.3`](https://github.com/rahuldave/smallwikiapp/commit/dab89136e205c1102c10ce98dd9b4bd9c3814543) the library's README
  - [`step-09.4`](https://github.com/rahuldave/smallwikiapp/commit/8e526cfa908bef1fff32429f795882eb734a103b) the library gets a copy of wikipedia.py
  - [`step-09.5`](https://github.com/rahuldave/smallwikiapp/commit/34f1041135a78b1015d73e8fcb2529102c5ccf9e) the library's docstring and User-Agent
  - [`step-09.6`](https://github.com/rahuldave/smallwikiapp/commit/8545346928730b73e69a52a7652ff4fbf15a333c) the app depends on wikirandom
  - [`step-09.7`](https://github.com/rahuldave/smallwikiapp/commit/78ab09579fdffcb2db04e83807817e2edba27ebe) the app uses wikirandom, and its own wikipedia.py goes
  - [`step-09.8`](https://github.com/rahuldave/smallwikiapp/commit/f2dd413c02c731553f8c103b0e6c892dac0fa2dc) the app no longer needs requests and pydantic
  - [`step-09.9`](https://github.com/rahuldave/smallwikiapp/commit/008e616610b0829196a2f61182e45255015b95c1) the tests of the library are named for it
  - [`step-09.10`](https://github.com/rahuldave/smallwikiapp/commit/259e6364a52f83993c797f66148281b04eb92060) the docs check counts the library
- **[step-10](https://github.com/rahuldave/smallwikiapp/tree/step-10) Build.** Each package builds into a wheel for PyPI, with a licence and a link to its source. The app accepts only wikirandom 0.1. The User-Agent of the library names the installed version.
  - [`step-10.1`](https://github.com/rahuldave/smallwikiapp/commit/7744a84a4715e6edb876e1c4f3255daf524dd07d) just build, a wheel and a source archive of each package
  - [`step-10.2`](https://github.com/rahuldave/smallwikiapp/commit/6e6d2844bc7a5b34605ad76b9e03e6631fa236be) the app needs wikirandom 0.1, not any wikirandom
  - [`step-10.3`](https://github.com/rahuldave/smallwikiapp/commit/522bcb94133654c1e72a9592c852681e0b5e2055) just lint-config checks the library's pyproject.toml too
  - [`step-10.4`](https://github.com/rahuldave/smallwikiapp/commit/2c03603dc72a212f1575459528b3d269bb52be0d) the library's licence and author, and both repository links
  - [`step-10.5`](https://github.com/rahuldave/smallwikiapp/commit/73fc4e12cc7a5831163e61fc01a3699355f95d52) the library's User-Agent says its installed version
<!-- steps:end -->

The walk through these steps, with its notes and slides, is in
[smallwikiapp-walk](https://github.com/rahuldave/smallwikiapp-walk).

## Licence

Apache-2.0: see [`LICENSE`](LICENSE).
