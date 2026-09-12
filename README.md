# spikeforge-hub

[![CI](https://github.com/capsize-games/spikeforge-hub/actions/workflows/ci.yml/badge.svg)](https://github.com/capsize-games/spikeforge-hub/actions/workflows/ci.yml)
[![Status: pre-1.0](https://img.shields.io/badge/status-pre--1.0-orange.svg)](https://github.com/capsize-games/spikeforge)
[![License: BSD-3-Clause](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](LICENSE)
[![Python 3.10–3.13](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-3776AB.svg)](https://www.python.org/downloads/)
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

`spikeforge-hub` is pre-1.0 and not yet published to PyPI (neither is its
`spikeforge` dependency). Until then, install both from source:

```bash
pip install "git+https://github.com/capsize-games/spikeforge.git@main#subdirectory=packages/spikeforge"
pip install "git+https://github.com/capsize-games/spikeforge-hub.git@main"
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
