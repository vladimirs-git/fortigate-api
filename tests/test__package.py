"""unittests package"""

import os
import re
import unittest
from datetime import datetime

from fortigate_api import __title__
from setup import PACKAGE_, ROOT


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

    # @unittest.skip("solve pylint conflict")
    def test_valid__init__(self):
        """__init__.py"""
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
        for meta in metadata:
            metadata2 = [s for s in lines2 if re.match(meta, s)]
            self.assertEqual(len(metadata2), 1, msg=f"invalid {meta=} in {path2=}")

    def test_valid__version(self):
        """version"""
        path = os.path.join(ROOT, PACKAGE_, "__init__.py")
        with open(path) as fh:
            text = fh.read()
            version_init = (re.findall("^__version__ = \"(.+)\"", text, re.M) or [""])[0]
            self.assertNotEqual(version_init, "", msg=f"__version__ in {path=}")

        path = os.path.join(ROOT, "setup.py")
        with open(path) as fh:
            text = fh.read()
            version_setup = (re.findall("^VERSION = \"(.+)\"", text, re.M) or [""])[0]
            self.assertNotEqual(version_setup, "", msg=f"VERSION in {path=}")

        self.assertRegex(version_init, version_setup, msg="the same version everywhere")
        regex = r"\d+(\.(\d+((a|b|c|rc)\d+)?|post\d+|dev\d+))+"
        version = version_init
        self.assertRegex(version, regex, msg="version naming convention")

        path = os.path.join(ROOT, "README.md")
        with open(path) as fh:
            text = fh.read()
            regex = __title__ + r"-(.+)\.tar\.gz"
            versions_readme = re.findall(regex, text, re.M)
            for version_readme in versions_readme:
                self.assertEqual(version_readme, version, msg=f"package name in {path=}")

        path = os.path.join(ROOT, "CHANGELOG.txt")
        with open(path) as fh:
            text = fh.readline().strip()
            version_changelog = (re.findall(r"(.+)\s\(\d\d\d\d-\d\d-\d\d\)$", text) or [""])[0]
            self.assertEqual(version_changelog, version, msg=f"version in {path=}")

    def test_valid__date(self):
        """__date__"""
        path = os.path.join(ROOT, PACKAGE_, "__init__.py")
        with open(path) as fh:
            # date format convention
            text = fh.read()
            date_ = (re.findall("^__date__ = \"(.+)\"", text, re.M) or [""])[0]
            msg = f"invalid __date__ in {path=}"
            self.assertRegex(date_, r"\d\d\d\d-\d\d-\d\d", msg=msg)

            # last modified file
            date_version = datetime.strptime(date_, "%Y-%m-%d").date()
            date_max = max([t[1] for t in self._paths_dates()])
            self.assertEqual(date_version, date_max, msg=msg)

            path = os.path.join(ROOT, "CHANGELOG.txt")
            with open(path) as fh_:
                line = fh_.readline().strip()
                date_changelog = (re.findall(r".+\s\((\d\d\d\d-\d\d-\d\d)\)$", line) or [""])[0]
                self.assertEqual(date_changelog, date_, msg=f"date in {path=}")


if __name__ == "__main__":
    unittest.main()
