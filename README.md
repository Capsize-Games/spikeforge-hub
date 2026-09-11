# spikeforge-hub

Curated spiking-neural-network model hub for
[spikeforge](https://github.com/capsize-games/spikeforge): the offline catalog
plus the cache, download, verification, and import funnel that turns a hub
entry into a loaded `spikeforge` model.

`spikeforge-hub` owns the `spikeforge_hub` import root:

- `spikeforge_hub.catalog` / `spikeforge_hub.entry` — the curated catalog and
  its schema.
- `spikeforge_hub.cache` / `spikeforge_hub.downloads` / `spikeforge_hub.hf_api`
  — on-disk cache and Hugging Face access.
- `spikeforge_hub.inspect` / `spikeforge_hub.compat` / `spikeforge_hub.import_model`
  — the inspect/compat/promote import funnel.
- `spikeforge_hub.cli` — the `spikeforge-hub` console script.

## Installation

```bash
pip install spikeforge-hub
```

## Development

```bash
pip install -e ".[dev,nir]"
ruff check .
pytest
```

## License

BSD-3-Clause. See [`LICENSE`](LICENSE).
