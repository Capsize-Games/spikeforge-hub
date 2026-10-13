# Fleet audit — spikeforge-hub

Fleet-audit record for
[Capsize-Games/spikeforge-hub#3](https://github.com/Capsize-Games/spikeforge-hub/issues/3).
Docs only. Verified against `main` on 2026-10-13
(`pyproject.toml` version `0.1.0`) and against `origin/main` of
`Capsize-Games/spikeforge` and PyPI on the same day.

## 1. Identity, boundary, owner, runtime

- **Canonical identity.** GitHub `Capsize-Games/spikeforge-hub`
  (public, default branch `main`); local checkout
  `Projects/spikeforge/spikeforge-hub`.
- **Owner and license.** Capsize LLC (`contact@capsizegames.com`),
  BSD-3-Clause. Public history; no rewrite or deletion is
  authorized by this audit.
- **Product boundary.** This repository owns the `spikeforge_hub`
  import root: the curated model catalog, cache, Hugging Face
  access, verification, and the inspect/compat/promote import
  funnel. Dependency direction is hub-to-core; the `spikeforge`
  core package never depends on the hub. The catalog
  (`models.json`) and curation policy (`CURATION.md`) are runtime
  data with offline-first behavior.
- **Supported runtimes.** Python `>=3.10`; CI runs the 3.10–3.13
  matrix on GitHub-hosted Ubuntu workers with CPU torch wheels.
- **Deployment channel: none from this repository.** The only
  workflow is `ci.yml`; there is no release workflow and no PyPI
  trusted publisher here. PyPI `spikeforge-hub` publishes from the
  monorepo (section 3). The README's "not yet published to PyPI"
  note and its install-from-standalone-`main` instructions are
  stale relative to PyPI and are recorded as drift, not fixed here.
- **Migration metadata.** `capsize.json` and `justfile` are present
  (`setup`/`build`/`test`/`lint`/`ci`); the local task contract in
  `AGENTS.md` matches them.

## 2. Dependency table (`pyproject.toml` @ 0.1.0)

| Dependency | Current here | Canonical (monorepo `packages/spikeforge-hub` @ 0.3.2) | Proposed authority |
| --- | --- | --- | --- |
| `spikeforge` | `~=0.3.0` | `~=0.5.2` | Monorepo; this pin is two minor lines stale |
| `torch` | `>=2.5` | `>=2.5` | Agreed; no change |
| `huggingface_hub` | `>=0.20` | `>=0.20` | Agreed; no change |
| `dev` (`pytest`, `pytest-cov`, `ruff`) | unpinned | unpinned | Agreed; no change |
| `nir` (`nir`, `nirtorch` `>=1.0`) | present | absent (no `nir` extra) | Standalone-only extra with no canonical counterpart; see section 4 |
| Console scripts | `spikeforge-hub` | `spikeforge-hub` plus `spikeforge-registry` | Monorepo owns the registry CLI |

ML/NIR framework dependencies stay explicit and hub-local in both
copies; nothing here is a candidate for `capsize-commons` (Python
utilities) or any frontend package.

## 3. Monorepo-canonical evidence

PyPI `spikeforge-hub` builds from monorepo
`packages/spikeforge-hub`, and this standalone repository is a stale
mirror of that source. Evidence, each item verified directly:

1. **Version lineage.** Standalone `main`: `0.1.0`. Monorepo
   `packages/spikeforge-hub/pyproject.toml` on `origin/main`:
   `0.3.2`. PyPI `spikeforge-hub` latest: `0.3.2`. The PyPI
   version equals the monorepo version, not the standalone one.
2. **Release path.** Monorepo `.github/workflows/release.yml`
   publishes `packages/<distribution>` to PyPI from
   `<distribution>-v<version>` tags via a per-distribution trusted
   publisher (the workflow names `spikeforge-hub` explicitly).
   This repository has no corresponding workflow.
3. **File counts.** Standalone `spikeforge_hub/`: **21** files.
   Monorepo `spikeforge_hub/`: **35** files (29 source/data plus 6
   `weights/*.pt` binaries). Files present only in the standalone:
   **none** — it is a strict subset.
4. **Monorepo-only files (14).** `account_cli.py`, `client.py`,
   `community.py`, `transfer.py`, `registry.py`,
   `registry_cli.py`, `registry_errors.py`, `py.typed`, and six
   `weights/*.pt` reference checkpoints.
5. **Shared-file drift.** 14 of the 21 shared files differ
   byte-for-byte. Example, `cli.py`: the monorepo copy adds the
   account subcommands (`login`, `whoami`, `push`, `pull`,
   `quota` wired from `account_cli`), a `--trained` list filter,
   and `add_version_flag`; the standalone copy has none of the
   three.
6. **Packaging drift.** Core pin `~=0.3.0` versus `~=0.5.2`;
   monorepo-only `spikeforge-registry` script; standalone-only
   `nir` extra; stale "not yet published" README claim.

## 4. Keep / migrate / retire and scope-guard close

- **Keep:** the package-boundary definition (hub owns catalog and
  network I/O; core never depends on hub), the offline-catalog
  behavior, and the `capsize.json`/`justfile` task contract. The
  standalone-only `nir` extra is kept as-is; removing or restoring
  it is a packaging decision for the canonical copy, not this
  mirror.
- **Migrate:** none. Every shared-code candidate in this repository
  already exists in a newer form at the canonical monorepo path, so
  there is no extraction with a consumer, API shape, and
  compatibility test to propose. A monorepo-to-mirror re-sync
  would run in the opposite direction and is out of scope here.
- **Retire:** none in this PR. This audit deletes nothing.

Per the issue's scope guard, the migration portion is **closed with
this evidence**: no extraction from this repository is warranted.
The mirror's own disposition (re-sync automation, README redirect,
or archive) is a follow-up decision left to the fleet coordinator;
this record authorizes none of those outcomes by itself.
