"""unittest policy.py"""

import unittest

from fortigate_api.policy import Policy
from tests.helper__tst import NAME3, POL1, POL3, MockFortigate


# noinspection DuplicatedCode
class Test(MockFortigate):
    """Policy"""

    def setUp(self):
        """setUp"""
        super().setUp()
        self.obj = Policy(rest=self.rest)

    def test_valid__create(self):
        """Policy.create()"""
        for name, req in [
            (POL1, 200),  # present in the Fortigate, no need create
            ("POL9", 500),  # error
            (NAME3, 200),  # absent in the Fortigate, need create
        ]:
            result = self.obj.create(data={"name": name}).status_code
            self.assertEqual(result, req, msg=f"{name=}")

    def test_valid__delete(self):
        """Policy.delete()"""
        for kwargs, req in [
            (dict(uid="1"), 200),
            (dict(uid=1), 200),
            (dict(uid="0"), 500),
            (dict(uid=9), 500),
            (dict(filter="policyid==1"), 200),
            (dict(filter="policyid==9"), 200),
            (dict(filter=f"name=={POL1}"), 200),
            (dict(filter="name==POL9"), 200),
            (dict(uid="", filter="policyid==1"), 200),
            (dict(uid=0, filter="policyid==1"), 200),
        ]:
            result = self.obj.delete(**kwargs).status_code
            self.assertEqual(result, req, msg=f"{kwargs=}")

    def test_invalid__delete(self):
        """Policy.delete()"""
        for kwargs, error in [
            (dict(uid=""), ValueError),
            (dict(uid=0), ValueError),
            (dict(uid=1, filter="policyid==1"), KeyError),
            (dict(uid="0", filter="policyid==1"), KeyError),
        ]:
            with self.assertRaises(error, msg=f"{kwargs=}"):
                self.obj.delete(**kwargs)

    def test_valid__get(self):
        """Policy.get()"""
        for kwargs, req in [
            ({}, [POL1, POL3]),
            (dict(uid=1), [POL1]),
            (dict(uid=9), []),
            (dict(uid=1, filter=f"name=={POL1}"), [POL1]),
            (dict(filter=f"name=={POL1}"), [POL1]),
            (dict(filter="name==POL9"), []),

            (dict(efilter="srcaddr==1.1.1.0/30"), [POL1]),
            (dict(efilter="srcaddr==1.1.1.0/29"), []),
            (dict(efilter="srcaddr!=1.1.1.0/30"), [POL3]),
            (dict(efilter="srcaddr!=1.1.1.0/29"), [POL1, POL3]),
            (dict(efilter="srcaddr<=1.1.1.0/32"), []),  # get all subnets
            (dict(efilter="srcaddr<=1.1.1.0/31"), []),
            (dict(efilter="srcaddr<=1.1.1.0/30"), [POL1]),
            (dict(efilter="srcaddr<=1.1.1.0/29"), [POL1]),
            (dict(efilter="srcaddr<=0.0.0.0/0"), [POL1, POL3]),
            (dict(efilter="srcaddr>=1.1.1.1"), [POL1]),  # get all supernets
            (dict(efilter="srcaddr>=1.1.1.0/32"), [POL1]),
            (dict(efilter="srcaddr>=1.1.1.0/31"), [POL1]),
            (dict(efilter="srcaddr>=1.1.1.0/30"), [POL1]),
            (dict(efilter="srcaddr>=1.1.1.0/29"), []),
            (dict(efilter="srcaddr>=0.0.0.0/0"), []),

            (dict(efilter="srcaddr==2.2.2.0/30"), []),
            (dict(efilter="srcaddr!=2.2.2.0/30"), [POL1, POL3]),
            (dict(efilter="srcaddr==3.3.3.0/30"), [POL3]),
            (dict(efilter="srcaddr<=3.3.3.0/30"), [POL3]),
            (dict(efilter="srcaddr!=3.3.3.0/30"), [POL1]),
            (dict(efilter="srcaddr==4.4.4.0/30"), []),
            (dict(efilter="srcaddr<=4.4.4.0/30"), []),
            (dict(efilter="srcaddr!=4.4.4.0/30"), [POL1, POL3]),
            (dict(efilter="srcaddr==5.5.5.0/30"), []),
            (dict(efilter="srcaddr<=5.5.5.0/30"), []),
            (dict(efilter="srcaddr!=5.5.5.0/30"), [POL1, POL3]),

            (dict(efilter="dstaddr==1.1.1.0/30"), []),
            (dict(efilter="dstaddr!=1.1.1.0/30"), [POL1, POL3]),
            (dict(efilter="dstaddr==2.2.2.0/30"), [POL1]),
            (dict(efilter="dstaddr<=2.2.2.0/32"), []),
            (dict(efilter="dstaddr<=2.2.2.0/31"), []),
            (dict(efilter="dstaddr<=2.2.2.0/30"), [POL1]),
            (dict(efilter="dstaddr<=2.2.2.0/29"), [POL1]),
            (dict(efilter="dstaddr==3.3.3.0/30"), []),
            (dict(efilter="dstaddr!=3.3.3.0/30"), [POL1, POL3]),
            (dict(efilter="dstaddr==4.4.4.0/30"), []),
            (dict(efilter="dstaddr!=4.4.4.0/30"), [POL1, POL3]),
            (dict(efilter="dstaddr<=5.5.5.0/30"), [POL3]),
            (dict(efilter="dstaddr!=5.5.5.0/30"), [POL1]),

            (dict(efilter=["srcaddr==1.1.1.0/30", "dstaddr==1.1.1.0/30"]), []),
            (dict(efilter=["srcaddr==1.1.1.0/30", "dstaddr==2.2.2.0/30"]), [POL1]),
            (dict(efilter=["srcaddr==1.1.1.0/30", "dstaddr<=2.2.2.0/30"]), [POL1]),
            (dict(efilter=["srcaddr==2.2.2.0/30", "dstaddr==3.3.3.0/30"]), []),
            (dict(efilter=["srcaddr==3.3.3.0/30", "dstaddr==5.5.5.0/30"]), [POL3]),

        ]:
            result_ = self.obj.get(**kwargs)
            result = [d["name"] for d in result_]
            self.assertEqual(result, req, msg=f"{kwargs=}")

    def test_invalid__get(self):
        """Policy.get()"""
        for kwargs, error in [
            (dict(name=POL1), KeyError),
            (dict(efilter="srcaddr=!1.1.1.0/30"), ValueError),
            (dict(efilter="typo==1.1.1.0/30"), ValueError),
            (dict(efilter="srcaddr==typo"), ValueError),
            (dict(efilter="srcaddr==1.1.1.1000"), ValueError),
            (dict(efilter="srcaddr==1.1.1.1/33"), ValueError),
            (dict(efilter="srcaddr==fd12:3456:789a:1::/64"), ValueError),
        ]:
            with self.assertRaises(error, msg=f"{kwargs=}"):
                self.obj.get(**kwargs)

    def test_valid__move(self):
        """Policy.move()"""
        for id_, position, neighbor, req in [
            (1, "before", 2, 200),
            (2, "before", 1, 500),
        ]:
            result = self.obj.move(uid=id_, position=position, neighbor=neighbor).status_code
            self.assertEqual(result, req, msg=f"{id_=} {position=} {neighbor=}")

    def test_valid__update(self):
        """Policy.update()"""
        for kwargs, req in [
            (dict(uid=1, data=dict(name=POL1, policyid=1)), 200),
            (dict(uid=9, data=dict(name="POL9", policyid=9)), 500),
            (dict(uid="1", data=dict(name=POL1, policyid=1)), 200),
            (dict(uid="9", data=dict(name="POL9", policyid=9)), 500),
            (dict(data=dict(name=POL1, policyid=1)), 200),
            (dict(data=dict(name="POL9", policyid=9)), 500),
        ]:
            result = self.obj.update(**kwargs).status_code
            self.assertEqual(result, req, msg=f"{kwargs=}")


if __name__ == "__main__":
    unittest.main()
