"""unittest fortigate_api"""

import os
import re
import unittest

import fortigate_api

ROOT = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
PACKAGE = os.path.split(ROOT)[1]
PACKAGE_ = PACKAGE.replace("-", "_")


class Test(unittest.TestCase):
    """unittest fortigate_api"""

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
        req_imports = {
            f"from {PACKAGE_}.api import FortigateAPI",
            f"from {PACKAGE_}.fortigate import Fortigate",
        }
        init_file = "__init__.py"
        filepath = os.path.join(ROOT, init_file)
        with open(filepath) as f:
            lines = {s.strip() for s in f.readlines()}
            result = req_imports.difference(lines)
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


if __name__ == "__main__":
    unittest.main()
