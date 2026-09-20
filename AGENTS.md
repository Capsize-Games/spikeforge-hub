# SpikeForge hub

This repository owns the `spikeforge_hub` package: the curated model catalog,
cache, Hugging Face access, verification, and import funnel. Keep those model
and network boundaries separate from the `spikeforge` core package; the core
does not depend on the hub.

The local task contract is `python -m compileall -q spikeforge_hub` for the
build check, `ruff check .` for lint, and `pytest` for tests. Install the
development extras with `pip install -e ".[dev,nir]"` after installing the
private `spikeforge` core dependency as described in `README.md`. The existing
CI job uses the repository-scoped `spikeforge-hub-ci` local runner and a
read-only deploy key for that private dependency; never replace it with a
broader credential or commit credential material.

The hub's model catalog and curation policy are runtime data. Changes to
catalog entries, download verification, cache paths, or promotion rules need
focused tests and must preserve the offline catalog behavior.
