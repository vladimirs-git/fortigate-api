"""unittest files"""

import os
import pathlib
import re
import unittest

import fortigate_api

ROOT = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
PACKAGE = os.path.split(ROOT)[1]
PACKAGE_ = PACKAGE.replace("-", "_")


class Test(unittest.TestCase):
    """unittest files"""

    def test_valid__fortigate_api(self):
        """fortigate_api"""
        self.assertEqual(PACKAGE, "fortigate-api")
        self.assertEqual(PACKAGE_, "fortigate_api")
        self.assertEqual(fortigate_api.__title__, PACKAGE)
        for name in [
            "Fortigate",
            "FortigateAPI",
        ]:
            result = bool(name in dir(fortigate_api))
            self.assertTrue(result, msg=f"{name=}")

    def test_valid__init__(self):
        """fortigate-api/__init__.py"""
        req_lines = [
            f"from {PACKAGE_}.api import FortigateAPI",
            f"from {PACKAGE_}.fortigate import Fortigate",
        ]
        filepath = os.path.join(ROOT, "__init__.py")
        text = pathlib.Path(filepath).read_text(encoding="utf-8")
        lines = {s.strip() for s in text.split("\n")}
        result = set(req_lines).difference(lines)
        self.assertEqual(len(result), 0, msg=f"mandatory lines in {filepath=}")

    def test_valid__fortigate_api__init(self):
        """fortigate-api/fortigate_api/__init__.py"""
        req_imports = [
            f"from {PACKAGE_}.api import FortigateAPI",
            f"from {PACKAGE_}.fortigate import Fortigate",
            "__version__ =.+",
            "__title__ =.+",
            "__summary__ =.+",
            "__author__ =.+",
            "__email__ =.+",
            "__url__ =.+",
            "__download_url__ =.+",
            "__license__ =.+",
        ]
        init_file = "__init__.py"
        filepath = os.path.join(ROOT, PACKAGE_, init_file)
        with open(filepath) as f:
            lines = {s.strip() for s in f.readlines()}
            results = list()
            for req in req_imports:
                for line in lines:
                    if re.search(req, line):
                        break
                else:
                    results.append(req)
            self.assertEqual(len(results), 0, msg=f"mandatory lines in {filepath=} {results=}")

    def test_valid__version(self):
        """version"""
        path = os.path.join(ROOT, PACKAGE_, "__init__.py")
        text = pathlib.Path(path).read_text(encoding="utf-8")
        version_init = (re.findall("^__version__ = \"(.+)\"", text, re.M) or [""])[0]
        self.assertNotEqual(version_init, "", msg=f"absent __version__ in {path=}")

        path = os.path.join(ROOT, "setup.py")
        text = pathlib.Path(path).read_text(encoding="utf-8")
        version_setup = (re.findall("^VERSION = \"(.+)\"", text, re.M) or [""])[0]
        self.assertNotEqual(version_setup, "", msg=f"absent VERSION in {path=}")

        self.assertEqual(version_init, version_setup, msg=f"version")


if __name__ == "__main__":
    unittest.main()
