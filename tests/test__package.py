"""unittests package"""

import re
import unittest
from pathlib import Path

import dictdiffer  # type: ignore
import tomli

from fortigate_api import helpers as h
from fortigate_api.base import IMPLEMENTED_OBJECTS


def _make_pyproject_d(root: Path) -> dict:
    """Return data of pyproject.toml"""
    path = Path.joinpath(root, "pyproject.toml")
    fh = path.open(mode="rb")
    pyproject_d = tomli.load(fh)
    return pyproject_d


ROOT = Path(__file__).parent.parent.resolve()
PYPROJECT = _make_pyproject_d(ROOT)


class Test(unittest.TestCase):
    """package"""

    def test_valid__version__readme(self):
        """version in README, URL"""
        package = PYPROJECT["tool"]["poetry"]["name"].replace("_", "-")
        readme_file = PYPROJECT["tool"]["poetry"]["readme"]
        dwl_url = PYPROJECT["tool"]["poetry"]["urls"]["Download URL"]
        readme_text = Path.joinpath(ROOT, readme_file).read_text()
        version_req = PYPROJECT["tool"]["poetry"]["version"]

        for key, text in [
            (readme_file, readme_text),
            ("pyproject.toml project.urls.DownloadURL", dwl_url),
        ]:
            is_regex_found = False
            for regex in [
                package + r".+/(.+?)\.tar\.gz",
                package + r"@(.+?)$",
            ]:
                versions = re.findall(regex, text, re.M)
                for version in versions:
                    is_regex_found = True
                    self.assertEqual(version, version_req, msg=f"version in {key}")
            self.assertEqual(is_regex_found, True, msg=f"absent {version_req} in {key}")

    def test_valid__version__changelog(self):
        """version in CHANGELOG"""
        version_toml = PYPROJECT["tool"]["poetry"]["version"]
        path = Path.joinpath(ROOT, "CHANGELOG.rst")
        text = path.read_text()
        regex = r"(.+)\s\(\d\d\d\d-\d\d-\d\d\)$"
        version_log = h.findall1(regex, text, re.M)
        self.assertEqual(version_log, version_toml, msg=f"version in {path=}")

    def test_valid__date(self):
        """last modified date in CHANGELOG"""
        path = Path.joinpath(ROOT, "CHANGELOG.rst")
        text = path.read_text()
        regex = r".+\((\d\d\d\d-\d\d-\d\d)\)$"
        date_changelog = h.findall1(regex, text, re.M)
        last_modified = h.last_modified_date(root=str(ROOT))
        self.assertEqual(date_changelog, last_modified, msg="last modified file")

    def test_valid__implemented_objects(self):
        """IMPLEMENTED_OBJECTS"""
        expected = set()
        paths = h.files_py(root=str(ROOT))
        for path in paths:
            text = Path(path).read_text()
            if url_ := h.findall1(r"super\(\).__init__\(.+url_obj=\"(.+?)\"", text):
                expected.add(url_)

        # in code
        actual = set(IMPLEMENTED_OBJECTS)
        diff = list(dictdiffer.diff(expected, actual))
        self.assertEqual([], diff, msg="base.py IMPLEMENTED_OBJECTS")

        # in readme
        readme_text = Path.joinpath(ROOT, PYPROJECT["tool"]["poetry"]["readme"]).read_text()
        actual = {s for s in IMPLEMENTED_OBJECTS if h.findall1(s, readme_text)}
        expected = set(IMPLEMENTED_OBJECTS)
        diff = list(dictdiffer.diff(expected, actual))
        self.assertEqual([], diff, msg="Readme IMPLEMENTED_OBJECTS")


if __name__ == "__main__":
    unittest.main()
