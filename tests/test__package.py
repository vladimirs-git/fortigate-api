"""unittests package"""

import os
import re
import unittest
from datetime import datetime

# noinspection PyProtectedMember
from fortigate_api import __title__
from setup import PACKAGE_, ROOT, README

CHANGELOG = "CHANGELOG.rst"


class Test(unittest.TestCase):
    """unittests package"""

    # =========================== helpers ============================

    @staticmethod
    def _paths_dates():
        """path to .py files with last modified dates"""
        paths = []
        for root_i, _, files_i in os.walk(ROOT):
            for file_ in files_i:
                if file_.endswith(".py"):
                    path = os.path.join(root_i, file_)
                    stat = os.stat(path)
                    date_ = datetime.fromtimestamp(stat.st_mtime).date()
                    paths.append((path, date_))
        return paths

    # ============================ tests =============================

    def test_valid__init__(self):
        """__init__.py"""
        metadata = [
            "__all__ = .+",
            "__version__ = .+",
            "__date__ = .+",
            "__title__ = .+",
            "__summary__ = .+",
            "__author__ = .+",
            "__email__ = .+",
            "__url__ = .+",
            "__download_url__ = .+",
            "__license__ = .+",
        ]
        path1 = os.path.join(ROOT, "__init__.py")
        path2 = os.path.join(ROOT, PACKAGE_, "__init__.py")
        with open(path1) as fh1, open(path2) as fh2:
            lines1 = {s.strip() for s in fh1.read().split("\n")}
            lines2 = {s.strip() for s in fh2.read().split("\n")}
            regex = r"(import|from)\s"
            imports1 = {s for s in lines1 if re.match(regex, s)}
            imports2 = {s for s in lines2 if re.match(regex, s)}
            diff = imports1.difference(imports2)
            self.assertEqual(len(diff), 0, msg=f"imports {diff=} in {path1=} {path2=}")

        for meta in metadata:
            metadata2 = [s for s in lines2 if re.match(meta, s)]
            self.assertEqual(len(metadata2), 1, msg=f"absent {meta=} in {path2=}")

    def test_valid__version(self):
        """version"""
        path = os.path.join(ROOT, PACKAGE_, "__init__.py")
        with open(path) as fh:
            text = fh.read()
            version = (re.findall("^__version__ = \"(.+)\"", text, re.M) or [""])[0]
            regex = r"\d+(\.(\d+((a|b|c|rc)\d+)?|post\d+|dev\d+))+"
            self.assertRegex(version, regex, msg=f"__version__ in {path=}")

        path = os.path.join(ROOT, "setup.py")
        with open(path) as fh:
            text = fh.read()
            version_setup = (re.findall("^VERSION = \"(.+)\"", text, re.M) or [""])[0]
            self.assertEqual(version_setup, version, msg=f"VERSION in {path=}")

        path = os.path.join(ROOT, README)
        with open(path) as fh:
            text = fh.read()
            regex = __title__ + r"-(.+)\.tar\.gz"
            versions_readme = re.findall(regex, text, re.M)
            for version_readme in versions_readme:
                self.assertEqual(version_readme, version, msg=f"version in {path=}")

        path = os.path.join(ROOT, CHANGELOG)
        with open(path) as fh:
            text = fh.read()
            regex = r"(.+)\s\(\d\d\d\d-\d\d-\d\d\)$"
            version_changelog = (re.findall(regex, text, re.M) or [""])[0]
            self.assertEqual(version_changelog, version, msg=f"version in {path=}")

    def test_valid__date(self):
        """__date__"""
        path = os.path.join(ROOT, PACKAGE_, "__init__.py")
        with open(path) as fh:
            text = fh.read()
            date = (re.findall("^__date__ = \"(.+)\"", text, re.M) or [""])[0]
            self.assertRegex(date, r"\d\d\d\d-\d\d-\d\d", msg=f"date in {path=}")

            # last modified file
            date_last = max([t[1] for t in self._paths_dates()])
            self.assertEqual(date, str(date_last), msg="last modified file")

            path = os.path.join(ROOT, CHANGELOG)
            with open(path) as fh_:
                text = fh_.read()
                regex = r".+\((\d\d\d\d-\d\d-\d\d)\)$"
                date_changelog = (re.findall(regex, text, re.M) or [""])[0]
                self.assertEqual(date_changelog, date, msg=f"date in {path=}")


if __name__ == "__main__":
    unittest.main()
