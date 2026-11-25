"""Release-policy guards: core pin, Python floor, and CI matrix."""

import re
from pathlib import Path

import tomllib

_ROOT = Path(__file__).resolve().parent.parent

_EXPECTED_CORE_PIN = "spikeforge~=0.6.3"
_EXPECTED_PYTHONS = ["3.11", "3.12", "3.13"]


def _project_table() -> dict:
    """Return the parsed ``[project]`` table of ``pyproject.toml``."""
    text = (_ROOT / "pyproject.toml").read_bytes()
    return tomllib.loads(text.decode("utf-8"))["project"]


def _requirement_name(requirement: str) -> str:
    """Return the bare distribution name of a requirement string."""
    for index, char in enumerate(requirement):
        if char in "<>=!~;[":
            return requirement[:index].strip()
    return requirement.strip()


def _ci_text() -> str:
    """Return the raw text of the CI workflow."""
    return (_ROOT / ".github" / "workflows" / "ci.yml").read_text(
        encoding="utf-8",
    )


def test_core_pin_tracks_family_matrix() -> None:
    """The core pin is the matrix compatible-release pin."""
    project = _project_table()
    pins = [
        dep
        for dep in project["dependencies"]
        if _requirement_name(dep) == "spikeforge"
    ]
    assert pins == [_EXPECTED_CORE_PIN]


def test_python_floor_matches_core() -> None:
    """The floor admits only interpreters the matrix core supports."""
    project = _project_table()
    assert "3.11" in project["requires-python"]
    assert "3.10" not in project["requires-python"]


def test_classifiers_exclude_python_310() -> None:
    """No classifier advertises an interpreter outside the matrix."""
    project = _project_table()
    joined = "\n".join(project["classifiers"])
    assert "Python :: 3.10" not in joined
    for version in _EXPECTED_PYTHONS:
        assert f"Python :: {version}" in joined


def test_supported_ml_deps_are_present() -> None:
    """The shared ML boundary stays explicit and hub-local."""
    project = _project_table()
    names = [_requirement_name(dep) for dep in project["dependencies"]]
    assert "torch" in names
    assert "huggingface_hub" in names
    nir = project["optional-dependencies"]["nir"]
    assert any(_requirement_name(dep) == "nir" for dep in nir)
    assert any(_requirement_name(dep) == "nirtorch" for dep in nir)


def test_ci_matrix_matches_supported_pythons() -> None:
    """CI provisions exactly the documented interpreter matrix."""
    match = re.search(r"python-version:\s*\[(.*?)\]", _ci_text())
    assert match is not None
    found = [part.strip().strip("\"'") for part in match.group(1).split(",")]
    assert found == _EXPECTED_PYTHONS


def test_ci_core_install_matches_pyproject_pin() -> None:
    """The CI core install line constrains the same pin as packaging."""
    assert f'pip install "{_EXPECTED_CORE_PIN}"' in _ci_text()


def test_release_doc_records_matrix_authority() -> None:
    """The ownership model names the monorepo matrix as authority."""
    doc = (_ROOT / "docs" / "RELEASE.md").read_text(encoding="utf-8")
    assert "compatibility.json" in doc
    assert "0.6.3" in doc
    assert "3.11" in doc
    assert "3.10" not in doc


def test_requirement_name_handles_extras_and_spaces() -> None:
    """Names parse through extras without raising on odd input."""
    assert _requirement_name("spikeforge[nir]~=0.6.3") == "spikeforge"
    assert _requirement_name("  torch>=2.5  ") == "torch"
    assert _requirement_name("") == ""
    assert _requirement_name("spikeforge") == "spikeforge"


def test_exact_equality_pin_is_not_the_matrix_pin() -> None:
    """An exact pin must fail the compatible-release guard."""
    assert _EXPECTED_CORE_PIN != "spikeforge==0.6.3"
    assert _requirement_name("spikeforge==0.6.3") == "spikeforge"
