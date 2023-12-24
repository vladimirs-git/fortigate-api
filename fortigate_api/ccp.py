"""CiscoConfParse adapted for Fortigate.

UNDER DEVELOPMENT!

Helper that parses the Fortigate config to find and change config commands.
For more details see https://github.com/mpenning/ciscoconfparse
"""
import re
from typing import List
from vhelpers import vre
from ciscoconfparse import CiscoConfParse, JunosCfgLine  # type: ignore

from fortigate_api import helpers as h
from fortigate_api.types_ import LStr, T2Str, T3Str, UStr

LJunosCfgLine = List[JunosCfgLine]


class FgtConfParse(CiscoConfParse):
    """CiscoConfParse adapted for Fortigate.

    UNDER DEVELOPMENT!
    """

    def __init__(self, config: UStr, comment="#", encoding="UTF-8", **kwargs):
        """FgtConfParse.

        :param config: Fortigate config.
        :type config: str or List[str]

        :param str comment: Comment delimiter. Default is `#`.

        :param kwargs: Other CiscoConfParse parameters.
        """
        config_: str = self._init_config(config)
        config_ = convert_fgt_to_junos(config_)
        lines = config_.splitlines()
        kwargs.update(
            config=lines,
            comment=comment,
            encoding=encoding,
            # todo logging INFO     | ciscoconfparse.ciscoconfparse:__init__:
            #  As of version 1.9.17 and later,
            #  `ignore_blank_lines=True` is only honored when `factory=True`
            # ignore_blank_lines=False,
            syntax="junos",
        )
        super().__init__(**kwargs)

    @staticmethod
    def _init_config(config: UStr) -> str:
        """Init Fortigate config."""
        if isinstance(config, str):
            return config
        if not isinstance(config, (list, tuple)):
            raise TypeError(f"{config=} {str} expected")
        for line in config:
            if not isinstance(line, str):
                raise TypeError(f"{line=} {str} expected")
        return "\n".join(config)


# ============================= function =============================

def convert_fgt_to_junos(config: str) -> str:
    """Convert Fortigate commands to Junos syntax, to parse by ciscoconfparse.

    :param config: Fortigate syntax config.

    :return config: CiscoConfParse junos syntax config.

    :example:
        config = "
            config system interface
              edit "mgmt"
                set ip 10.0.0.1 255.255.255.0
              next
            end
           "
        convert_fgt_to_junos(config) -> "
            config system interface {
              edit "mgmt" {
                set ip 10.0.0.1 255.255.255.0
              }
              next
            }
            end
           "
    """
    spaces = r"^(\s+)?"
    re_config = f"({spaces}config .+)"
    re_end = f"{spaces}(end)"
    re_edit = f"({spaces}edit .+)"
    re_next = f"{spaces}(next)"
    re_comment = f"$|{spaces}#"

    fgt_lines: LStr = [s.rstrip() for s in config.splitlines()]
    fgt_lines = [s for s in fgt_lines if not re.match(re_comment, s)]

    junos_lines: LStr = []
    for line in fgt_lines:
        # config
        if re.match(re_config, line):
            line += " {"
        # end
        elif re.match(re_end, line):
            result = re.findall(re_end, line)
            indent, _ = result[0][:2]
            line = indent + "}\n" + indent + "end"
        # edit
        elif re.match(re_edit, line):
            line += " {"
        # next
        elif re.match(re_next, line):
            result = re.findall(re_next, line)
            indent, _ = result[0][:2]
            line = indent + "}\n" + indent + "next"
        junos_lines.append(line)

    return "\n".join(junos_lines)


def findall(regex: str, obj: JunosCfgLine, flags=0) -> LStr:
    """Parse substrings from JunosCfgLine objects by regex.

    :param str regex: Regex pattern with 1 group.

    :param JunosCfgLine obj: JunosCfgLine object.

    :param int flags: re.findall flags.

    :return: List of interested substrings.
    :rtype: List[str]
    """
    string = "\n".join(obj.ioscfg)
    values = re.findall(pattern=regex, string=string, flags=flags)
    return values


def findall1(regex: str, obj: JunosCfgLine, flags=0) -> str:
    """Parse substring from JunosCfgLine objects by regex.

    :param str regex: Regex pattern with 1 group.

    :param JunosCfgLine obj: JunosCfgLine object.
    :param int flags: re.findall flags.

    :return: Interested substring.
    :rtype: str
    """
    value = ""
    for item in obj.ioscfg:
        if value := vre.find1(pattern=regex, string=item, flags=flags):
            break
    return value


def findall2(regex: str, obj: JunosCfgLine, flags=0) -> T2Str:
    """Parse 2 substrings from JunosCfgLine objects by regex.

    :param str regex: Regex pattern with 2 groups.

    :param JunosCfgLine obj: JunosCfgLine object.

    :param int flags: re.findall flags.

    :return: Interested substrings.
    """
    value1, value2 = "", ""
    for item in obj.ioscfg:
        value1, value2 = vre.find2(pattern=regex, string=item, flags=flags)
        if value1:
            break
    return value1, value2


def findall3(regex: str, obj: JunosCfgLine) -> T3Str:
    """Parse 3 substrings from JunosCfgLine objects by regex.

    :param str regex: Regex pattern with 3 groups.

    :param JunosCfgLine obj: JunosCfgLine object.

    :return: Interested substrings.
    """
    value1, value2, value3 = "", "", ""
    for item in obj.ioscfg:
        value1, value2, value3 = vre.find3(pattern=regex, string=item)
        if value1:
            break
    return value1, value2, value3


def find_by_keys(ccp: CiscoConfParse, keys: LStr) -> LJunosCfgLine:
    r"""Find object by keys in geneology.

    :param CiscoConfParse ccp: CiscoConfParse object.

    :param list keys: Geneology keys to find object.

    :return: List of JunosCfgLine objects.
    :rtype: List[JunosCfgLine]

    :example:
        keys = ["config system global", "edit \"wan1\""]
        find_by_keys(ccp, keys) -> [<JunosCfgLine # 20 '    edit "wan1"' (parent is # 21)>]
    """
    if not keys:
        return []
    *keys_parent, key_last = keys
    spaces = r"^(\s+)?"
    regex = f"{spaces}{key_last}$"

    objs_w_child: LJunosCfgLine = []
    for obj_ in ccp.find_objects(regex):
        if isinstance(obj_, JunosCfgLine):
            objs_w_child.append(obj_)

    results: LJunosCfgLine = []
    for obj in objs_w_child:
        all_parents: LStr = [o.text.strip() for o in obj.all_parents]
        if keys_parent == all_parents:
            results.append(obj)
    return results


def find_by_re_keys(ccp: CiscoConfParse, keys: LStr) -> LJunosCfgLine:
    """Find object by keys regex in geneology.

    :param CiscoConfParse ccp: CiscoConfParse object.

    :param list keys: Geneology regex keys to find object.

    :return: List of JunosCfgLine objects.
    :rtype: List[JunosCfgLine]

    :example:
        keys = ["config system global", r"edit .wan[12]."]
        find_by_keys(ccp, keys) -> [<JunosCfgLine # 20 '    edit "wan1"' (parent is # 21)>,
                                    <JunosCfgLine # 30 '    edit "wan2"' (parent is # 31)>]
    """
    if not keys:
        return []
    *re_parents, re_last = keys

    keys_last = []
    for line in ccp.ioscfg:
        if re.search(re_last, line):
            if line not in keys_last:
                keys_last.append(line)

    objs_w_child: LJunosCfgLine = []
    for key_last in keys_last:
        for obj_ in ccp.find_objects(key_last):
            if isinstance(obj_, JunosCfgLine):
                objs_w_child.append(obj_)

    results: LJunosCfgLine = []
    for obj in objs_w_child:
        all_parents: LStr = [o.text for o in obj.all_parents]
        if len(re_parents) == len(all_parents):
            if not re_parents:
                results.append(obj)
                continue
            for idx, re_parent in enumerate(re_parents):
                parent = all_parents[idx]
                if re.search(re_parent, parent):
                    results.append(obj)
                    break
    return results


def find_children(ccp: CiscoConfParse, keys: LStr) -> LJunosCfgLine:
    r"""Find children object by geneology keys.

    :param CiscoConfParse ccp: CiscoConfParse object.

    :param list keys: Geneology keys to find object.

    :return: List of children JunosCfgLine objects.
    :rtype: List[JunosCfgLine]

    :example:
        keys = ["config system global", "edit \"wan1\""]
        find_children(ccp, keys) -> ["set vdom \"root\"",
                                     "set ip 10.0.1.1 255.255.255.0",
                                     ...]
    """
    return [o for oo in find_by_keys(ccp, keys) for o in oo.children]


def join_children(obj: JunosCfgLine) -> str:
    """Join all children of JunosCfgLine object.

    :param JunosCfgLine obj: JunosCfgLine object.
    :return: joined text lines of all children.
    :rtype: str
    """
    lines = [o.text for o in obj.all_children]
    return "\n".join(lines)


def find_re_blocks(ccp: CiscoConfParse, regex: str) -> LStr:
    r"""Work similar to CiscoConfParse.find_block(), but return list of config sections".

    :param CiscoConfParse ccp: CiscoConfParse object.

    :param str regex: Regex pattern to find.

    :return: Lines of all_children in found block.

    :example:
        regex = "edit \"wan1\""
        find_children(ccp, keys) -> ["set vdom \"root\"",
                                     "set ip 10.0.1.1 255.255.255.0",
                                     ...]
    """
    blocks: LStr = []
    parents: LJunosCfgLine = ccp.find_objects(regex)
    for parent in parents:
        all_children: LStr = [o.text for o in parent.all_children]
        all_children.insert(0, parent.text)
        block = "\n".join(all_children)
        blocks.append(block)
    return blocks
