"""unittests package"""
import re
import unittest
from pathlib import Path

import dictdiffer  # type: ignore
import tomli
from vhelpers import vre

from fortigate_api import helpers as h
from fortigate_api.base import IMPLEMENTED_OBJECTS


def _make_pyproject_d(root: Path) -> dict:
    """Return data of pyproject.toml"""
    path = Path.joinpath(root, "pyproject.toml")
    fh = path.open(mode="rb")
    pyproject_d = tomli.load(fh)
    return pyproject_d


ROOT = Path(__file__).parent.parent.resolve()
PYPROJECT_D = _make_pyproject_d(ROOT)


class Test(unittest.TestCase):
    """package"""

    def test_valid__version__readme(self):
        """version in README, URL."""
        expected = PYPROJECT_D["tool"]["poetry"]["version"]
        package = PYPROJECT_D["tool"]["poetry"]["name"].replace("_", "-")
        readme = PYPROJECT_D["tool"]["poetry"]["readme"]
        readme_text = Path.joinpath(ROOT, readme).read_text(encoding="utf-8")
        url_toml = "pyproject.toml project.urls.DownloadURL"
        url_text = PYPROJECT_D["tool"]["poetry"]["urls"]["Download URL"]

        for source, text in [
            (readme, readme_text),
            (url_toml, url_text),
        ]:
            regexes = [fr"{package}.+/(.+?)\.tar\.gz", fr"{package}@(.+?)$"]
            versions = [v for s in regexes for v in re.findall(s, text, re.M)]
            assert expected in versions, f"version {expected} not in {source}"

    def test_valid__version__changelog(self):
        """version in CHANGELOG"""
        version_toml = PYPROJECT_D["tool"]["poetry"]["version"]
        path = Path.joinpath(ROOT, "CHANGELOG.rst")
        text = path.read_text(encoding="utf-8")
        regex = r"(.+)\s\(\d\d\d\d-\d\d-\d\d\)$"
        version_log = vre.find1(regex, text, re.M)
        self.assertEqual(version_log, version_toml, msg=f"version in {path=}")

    def test_valid__date(self):
        """last modified date in CHANGELOG"""
        path = Path.joinpath(ROOT, "CHANGELOG.rst")
        text = path.read_text(encoding="utf-8")
        regex = r".+\((\d\d\d\d-\d\d-\d\d)\)$"
        date_changelog = vre.find1(regex, text, re.M)
        last_modified = h.last_modified_date(root=str(ROOT))
        self.assertEqual(date_changelog, last_modified, msg="last modified file")

    def test_valid__implemented_objects(self):
        """IMPLEMENTED_OBJECTS"""
        expected = set()
        paths = h.files_py(root=str(ROOT))
        for path in paths:
            text = Path(path).read_text(encoding="utf-8")
            if url_ := vre.find1(r"super\(\).__init__\(.+url_obj=\"(.+?)\"", text):
                expected.add(url_)

        # in code
        actual = set(IMPLEMENTED_OBJECTS)
        diff = list(dictdiffer.diff(expected, actual))
        self.assertEqual([], diff, msg="base.py IMPLEMENTED_OBJECTS")

        # in readme
        path = Path.joinpath(ROOT, PYPROJECT_D["tool"]["poetry"]["readme"])
        readme_text = path.read_text(encoding="utf-8")
        actual = {s for s in IMPLEMENTED_OBJECTS if vre.find1(s, readme_text)}
        expected = set(IMPLEMENTED_OBJECTS)
        diff = list(dictdiffer.diff(expected, actual))
        self.assertEqual([], diff, msg="Readme IMPLEMENTED_OBJECTS")


if __name__ == "__main__":
    unittest.main()
