# spikeforge-hub

[![CI](https://github.com/capsize-games/spikeforge-hub/actions/workflows/ci.yml/badge.svg)](https://github.com/capsize-games/spikeforge-hub/actions/workflows/ci.yml)
[![Discord](https://img.shields.io/badge/Discord-Join%20the%20community-5865F2?logo=discord&logoColor=white)](https://capsizegames.com/discord)
[![Status: pre-1.0](https://img.shields.io/badge/status-pre--1.0-orange.svg)](https://github.com/capsize-games/spikeforge)
[![License: BSD-3-Clause](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](LICENSE)
[![Python 3.11–3.13](https://img.shields.io/badge/python-3.11%20%7C%203.12%20%7C%203.13-3776AB.svg)](https://www.python.org/downloads/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/capsize-games/spikeforge/blob/main/CONTRIBUTING.md)

Curated spiking-neural-network model hub for
[spikeforge](https://github.com/capsize-games/spikeforge): the offline catalog
plus the cache, download, verification, and import funnel that turns a hub
entry into a loaded `spikeforge` model.

`spikeforge-hub` owns the `spikeforge_hub` import root:

- `spikeforge_hub.catalog` / `spikeforge_hub.entry` — the curated catalog and
  its schema. See [`spikeforge_hub/CURATION.md`](spikeforge_hub/CURATION.md)
  for the policy that decides what may be added to it.
- `spikeforge_hub.cache` / `spikeforge_hub.downloads` / `spikeforge_hub.hf_api`
  — on-disk cache and Hugging Face access.
- `spikeforge_hub.inspect` / `spikeforge_hub.compat` / `spikeforge_hub.import_model`
  — the inspect/compat/promote import funnel.
- `spikeforge_hub.cli` — the `spikeforge-hub` console script.

## Installation

```bash
pip install spikeforge-hub
```

`spikeforge-hub` is pre-1.0. The canonical release publisher is the
[`spikeforge` monorepo](https://github.com/Capsize-Games/spikeforge):
PyPI `spikeforge-hub` builds from `packages/spikeforge-hub` there, and the
supported dependency matrix is recorded in [`docs/RELEASE.md`](docs/RELEASE.md)
(canonical authority: `compatibility.json` in the monorepo). This repository
is a source mirror of that path at `0.1.0`; install the matrix core first:

```bash
pip install "spikeforge~=0.6.3"
pip install "git+https://github.com/capsize-games/spikeforge-hub.git@main"
```

If the PyPI window is paused, fall back to the monorepo source for core:

```bash
pip install "git+https://github.com/capsize-games/spikeforge.git@main#subdirectory=packages/spikeforge"
```

## Development

```bash
pip install "git+https://github.com/capsize-games/spikeforge.git@main#subdirectory=packages/spikeforge"
pip install -e ".[dev,nir]"
ruff check .
pytest
```

## License

BSD-3-Clause. See [`LICENSE`](LICENSE). `spikeforge-hub` is an extracted
component of the `spikeforge` toolkit rather than an independent research
artifact, so it has no `CITATION.cff` of its own — to cite the project, use
the [`spikeforge` repository](https://github.com/capsize-games/spikeforge).
