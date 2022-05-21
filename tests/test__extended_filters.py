"""unittest extended_filters.py"""

import unittest

from fortigate_api import extended_filters
from tests.helper__tst import MockFortigate


class Test(MockFortigate):
    """unittest extended_filters.py"""

    def test_valid__valid_efilters(self):
        """Policy._valid_efilters()"""
        for efilters in [
            ["srcaddr==1.1.1.1/32"],
            ["srcaddr!=1.1.1.1/32"],
            ["srcaddr<=1.1.1.1/32"],
            ["srcaddr>=1.1.1.1/32"],
            ["dstaddr==1.1.1.1/32"],
            ["dstaddr!=1.1.1.1/32"],
            ["dstaddr<=1.1.1.1/32"],
            ["dstaddr>=1.1.1.1/32"],
            ["srcaddr==1.1.1.1/32", "dstaddr==2.2.2.2/32"],
        ]:
            extended_filters._valid_efilters(efilters=efilters)

    def test_invalid__valid_efilters(self):
        """Policy._valid_efilters()"""
        for efilters, error in [
            (["srcaddr!!1.1.1.1/32"], ValueError),
            (["typo==1.1.1.1/32"], ValueError),
            (["srcaddr==1.1.1.1/32", "srcaddr==2.2.2.2/32"], ValueError),
        ]:
            with self.assertRaises(error, msg=f"{efilters=}"):
                extended_filters._valid_efilters(efilters=efilters)


if __name__ == "__main__":
    unittest.main()
