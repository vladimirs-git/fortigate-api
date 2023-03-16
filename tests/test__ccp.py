"""unittest ccp.py"""

import unittest

from fortigate_api import ccp
from tests.helpers__ccp import (
    BLOCK_A1,
    BLOCK_A2,
    BLOCK_E2,
    CONFIG_FGT,
    CONFIG_FGT_DUMMY,
    CONFIG_JFGT,
    CONFIG_JFGT_DUMMY,
    CONFIG_JFGT_DUMMY2,
    CONFIG_JUNOS,
    JOINED1,
    JOINED2,
)


# noinspection DuplicatedCode
class Test(unittest.TestCase):
    """ccp.py"""

    def test_valid__init__(self):
        """FgtConfParse.__init__()"""
        for config, expected in [
            (CONFIG_FGT_DUMMY, CONFIG_JFGT_DUMMY2),
        ]:
            ccp_o = ccp.FgtConfParse(config=config)
            actual = "\n".join(ccp_o.ioscfg)
            self.assertEqual(actual, expected)

            obj = ccp_o.ConfigObjs.all_parents[0]
            actual = str(obj)
            self.assertEqual(actual, "<JunosCfgLine # 0 'config system A1'>")

    def test_valid__convert_fgt_to_junos(self):
        """ccp.convert_fgt_to_junos()"""
        for config, expected in [
            ("", ""),
            (CONFIG_FGT_DUMMY, CONFIG_JFGT_DUMMY),
            (CONFIG_FGT, CONFIG_JFGT),
        ]:
            actual = ccp.convert_fgt_to_junos(config=config)
            self.assertEqual(expected, actual, msg=f"{config=}")

    def test_valid__findall(self):
        """ccp.findall()"""
        lines = CONFIG_FGT_DUMMY.splitlines()
        ccp_o = ccp.FgtConfParse(config=lines)
        obj = ccp_o.ConfigObjs.all_parents[3]

        for regex, expected in [
            ("(typo)", []),
            (r"edit (E\d)", ["E1", "E2"]),
        ]:
            actual = ccp.findall(regex=regex, obj=obj)
            self.assertEqual(expected, actual, msg=f"{regex=}")

    def test_valid__findall1(self):
        """ccp.findall1()"""
        lines = CONFIG_FGT_DUMMY.splitlines()
        ccp_o = ccp.FgtConfParse(config=lines)
        obj = ccp_o.ConfigObjs.all_parents[3]

        for regex, expected in [
            ("(typo)", ""),
            (r"edit (E\d)", "E1"),
        ]:
            actual = ccp.findall1(regex=regex, obj=obj)
            self.assertEqual(expected, actual, msg=f"{regex=}")

    def test_valid__findall2(self):
        """ccp.findall2()"""
        lines = CONFIG_FGT_DUMMY.splitlines()
        ccp_o = ccp.FgtConfParse(config=lines)
        obj = ccp_o.ConfigObjs.all_parents[3]

        for regex, expected in [
            ("(typo)(typo)", ("", "")),
            (r"edit (E)(\d)", ("E", "1")),
        ]:
            actual = ccp.findall2(regex=regex, obj=obj)
            self.assertEqual(expected, actual, msg=f"{regex=}")

    def test_valid__findall3(self):
        """ccp.findall3()"""
        lines = CONFIG_FGT_DUMMY.splitlines()
        ccp_o = ccp.FgtConfParse(config=lines)
        obj = ccp_o.ConfigObjs.all_parents[3]

        for regex, expected in [
            ("(typo)(typo)(typo)", ("", "", "")),
            (r"(edit)\s+(E)(\d)", ("edit", "E", "1")),
        ]:
            actual = ccp.findall3(regex=regex, obj=obj)
            self.assertEqual(expected, actual, msg=f"{regex=}")

    def test_valid__find_by_keys__junos(self):
        """ccp.find_by_keys() for junos"""
        lines = CONFIG_JUNOS.splitlines()
        ccp_o = ccp.CiscoConfParse(config=lines, comment="#", syntax="junos")

        for keys, exp_parents, expected in [
            ([], [], []),
            (["A1"], [], ["A1"]),
            (["A2"], [], []),
            (["A1", "B1"], ["A1"], ["B1"]),
            (["A1", "B2"], ["A1"], ["B2"]),
            (["A1", "B1", "C1"], ["A1", "B1"], ["C1"]),
            (["A1", "B1", "C2"], ["A1", "B1"], ["C2"]),
            (["A1", "B1", "C1", "D2"], ["A1", "B1", "C1"], ["D2"]),
        ]:
            actual_lo = ccp.find_by_keys(ccp=ccp_o, keys=keys)

            actual_parents = [o.text.strip() for lo in actual_lo for o in lo.all_parents]
            self.assertEqual(exp_parents, actual_parents, msg=f"{keys=}")
            actual = [o.text.strip() for o in actual_lo]
            self.assertEqual(expected, actual, msg=f"{keys=}")

    def test_valid__find_by_keys__fgt(self):
        """ccp.find_by_keys() for Fortigate"""
        ccp_o = ccp.FgtConfParse(config=CONFIG_FGT_DUMMY)

        for keys, exp_parents, expected in [
            ([], [], []),
            (["config system A1"], [], ["config system A1"]),
            (["config system A2"], [], ["config system A2"]),
            (["config system typo"], [], []),
            (["config system A1", "set value B1"], ["config system A1"], ["set value B1"]),
            (["config system A2", "edit \"B1\""], ["config system A2"], ["edit \"B1\""]),
            (["config system A2", "edit \"B1\"", "set value \"C1\""],
             ["config system A2", "edit \"B1\""], ["set value \"C1\""]),
            (["config system A3", "edit B1", "config D-1", "edit E2"],
             ["config system A3", "edit B1", "config D-1"], ["edit E2"]),
        ]:
            objs = ccp.find_by_keys(ccp=ccp_o, keys=keys)
            actual = [o.text.strip() for lo in objs for o in lo.all_parents]
            self.assertEqual(exp_parents, actual, msg=f"{keys=}")
            actual = [o.text.strip() for o in objs]
            self.assertEqual(expected, actual, msg=f"{keys=}")

    def test_valid__find_children(self):
        """ccp.find_children()"""
        ccp_o = ccp.FgtConfParse(config=CONFIG_FGT_DUMMY)

        for keys, expected in [
            ([], []),
            (["config system A1"],
             ["set value B1", "set buffer \"", "line B2 1", "line B2 2", "\""]),
            (["config system A2", "set value B1"], []),
            (["config system A2", "set buffer \""], []),
            (["config system A2", "edit \"B1\""], ["set value \"C1\""]),
            (["config system A2", "edit \"B1\"", "set value \"C1\""], []),
            (["config system A3", "edit B1", "config D-1", "edit E2"], ["set value F1"]),
        ]:
            objs = ccp.find_children(ccp=ccp_o, keys=keys)
            actual = [o.text.strip() for o in objs]
            self.assertEqual(expected, actual, msg=f"{keys=}")

    def test_valid__join_children(self):
        """ccp.join_children()"""
        lines = CONFIG_FGT_DUMMY.splitlines()
        ccp_o = ccp.FgtConfParse(config=lines)
        parent1 = ccp_o.ConfigObjs.all_parents[1]
        parent2 = ccp_o.ConfigObjs.all_parents[2]
        for parent, expected in [
            (parent1, JOINED1),
            (parent2, JOINED2),
        ]:
            actual = ccp.join_children(obj=parent)
            self.assertEqual(expected, actual, msg=f"{parent=}")

    def test_valid__find_re_blocks(self):
        """ccp.find_re_blocks()"""
        lines = CONFIG_FGT_DUMMY.splitlines()
        ccp_o = ccp.FgtConfParse(config=lines)

        for regex, expected in [
            ("config system A[12]", [BLOCK_A1, BLOCK_A2]),
            ("edit E2", [BLOCK_E2]),
        ]:
            actual = ccp.find_re_blocks(ccp=ccp_o, regex=regex)
            self.assertEqual(expected, actual, msg=f"{regex=}")

    def test_valid__find_by_re_keys(self):
        """ccp.find_by_re_keys() for Fortigate"""
        ccp_o = ccp.FgtConfParse(config=CONFIG_FGT_DUMMY)

        for keys, exp_parents, expected in [
            ([], [], []),
            (["config system A[1]"], [], ["config system A1"]),
            (["config system A[12]"], [], ["config system A1", "config system A2"]),
            ([r"config system A\d", r"set value B\d"], ["config system A1"], ["set value B1"]),
            ([r"config system A\d", r"edit B\d", r"config D.+", r"edit E\d"],
             ["config system A3", "edit B1", "config D-1",
              "config system A3", "edit B1", "config D-1"], ["edit E1", "edit E2"]),
        ]:
            objs = ccp.find_by_re_keys(ccp=ccp_o, keys=keys)
            actual = [o.text.strip() for lo in objs for o in lo.all_parents]
            self.assertEqual(exp_parents, actual, msg=f"{keys=}")
            actual = [o.text.strip() for o in objs]
            self.assertEqual(expected, actual, msg=f"{keys=}")


if __name__ == "__main__":
    unittest.main()
