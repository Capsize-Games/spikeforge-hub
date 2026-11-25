# Release and ownership policy — spikeforge-hub

## Ownership

The canonical publisher of `spikeforge-hub` is the
[`Capsize-Games/spikeforge`](https://github.com/Capsize-Games/spikeforge)
monorepo. PyPI `spikeforge-hub` builds from `packages/spikeforge-hub` there
via the monorepo `release.yml` trusted publisher on tags
`<distribution>-v<version>`. This repository (`Capsize-Games/spikeforge-hub`)
is a source mirror of that path at `0.1.0`; it has no release workflow and
publishes nothing itself.

## Canonical authority

The supported family matrix is `compatibility.json` in the monorepo. Its
latest row pins the set this mirror tracks:

| Distribution | Version |
| --- | --- |
| `spikeforge` (core) | `0.6.3` |
| `spikeforge-hub` (canonical) | `0.5.2` |
| `spikeforge-targets` | `0.2.4` |

The release gate refuses to publish a non-core distribution whose core pin
is not exactly `spikeforge~=<matrix core version>`, so this mirror's
`pyproject.toml` pin (`spikeforge~=0.6.3`) tracks the matrix row above.

## Supported ML/runtime matrix

| Axis | Supported |
| --- | --- |
| Python | `3.11`, `3.12`, `3.13` (`requires-python >=3.11`, matching core) |
| `torch` | `>=2.5` (CPU wheels in CI via `TORCH_INDEX_URL`) |
| `torchvision` | `>=0.20` (installed from the same CPU index; avoids ABI mismatch) |
| `huggingface_hub` | `>=0.20` (isolated in `spikeforge_hub.probe`; offline catalog works without it) |
| `nir` / `nirtorch` | `>=1.0` each, via the `nir` extra (tests use `pytest.importorskip("nir")`) |
| `norse` / `lava` | Not hub dependencies; they live on `spikeforge-targets` extras |

## Reproducing the matrix in CI

`.github/workflows/ci.yml` provisions the `3.11`–`3.13` matrix, installs
CPU `torch` + `torchvision` first, then `spikeforge~=0.6.3` (falling back to
the public monorepo source when the PyPI window is paused), then
`pip install -e ".[dev,nir]"`, then `ruff check .` and `pytest`.
`tests/test_release_policy.py` guards the pin, the Python floor, and the
CI matrix against drift.
