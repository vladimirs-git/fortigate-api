"""Test package"""
import ast
import re
from pathlib import Path

from vhelpers import vdate, vdict, vpath, vre

ROOT = Path(__file__).parent.parent.resolve()
PYPROJECT_D = vdict.pyproject_d(ROOT)


def test__python_version():
    """Python version in pyproject.toml."""
    actual = PYPROJECT_D["tool"]["poetry"]["dependencies"]["python"]
    expected = "^3.8"
    assert actual == expected


def test__version__changelog():
    """Version in CHANGELOG."""
    path = Path.joinpath(ROOT, "CHANGELOG.rst")
    text = path.read_text(encoding="utf-8")
    regex = r"(.+)\s\(\d\d\d\d-\d\d-\d\d\)$"
    actual = vre.find1(regex, text, re.M)

    expected = PYPROJECT_D["tool"]["poetry"]["version"]
    assert actual == expected, f"version in {path=}"


def test__version__docs():
    """Version in docs/config.py."""
    path = Path.joinpath(ROOT, "docs", "conf.py")
    code = path.read_text(encoding="utf-8")
    tree = ast.parse(code)

    actual = ""
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "release":
                    # noinspection PyTypeChecker
                    actual = ast.literal_eval(node.value)
                    break

    expected = PYPROJECT_D["tool"]["poetry"]["version"]
    assert actual == expected, f"version in {path=}"


def test__last_modified_date():
    """Last modified date in CHANGELOG."""
    path = Path.joinpath(ROOT, "CHANGELOG.rst")
    text = path.read_text(encoding="utf-8")
    regex = r".+\((\d\d\d\d-\d\d-\d\d)\)$"
    actual = vre.find1(regex, text, re.M)
    files = vpath.get_files(ROOT, pattern="\.py$")
    expected = vdate.last_modified(files)
    assert actual == expected, "last modified file"
