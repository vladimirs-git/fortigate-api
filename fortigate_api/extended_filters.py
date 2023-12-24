"""Extended Filters."""
import logging
from collections import Counter
from functools import wraps
from ipaddress import ip_network, IPv4Network
from typing import Tuple

from vhelpers import vre

from fortigate_api import helpers as h
from fortigate_api.address import Address
from fortigate_api.address_group import AddressGroup
from fortigate_api.types_ import LDAny, LStr, DLStr, DLInet

EFILTER_KEYS = ["dstaddr", "srcaddr"]
EFILTER_OPERATORS = [
    "==",  # equal
    "!=",  # not equal
    ">=",  # supernets of interested prefix
    "<=",  # subnets of interested prefix
]


def wrap_efilters(func):
    """Wrap Extended Filters."""

    # noinspection PyIncorrectDocstring
    @wraps(func)
    def wrapper(fgt_api, **kwargs):
        """Wrap Extended Filters.

        :param FortigateAPI fgt_api: Wrapped object.

        :param efilter: Extended filter: `srcaddr`, `dstaddr` by condition: equals `==`,
            not equals `!=`,  supernets `>=`, subnets `<=`.
        :type efilter: str or List[str]

        :param kwargs: Parameters for wrapped object.

        :return: List of the fortigate-objects.
        :rtype: List[dict]
        """
        if efilters := h.pop_lstr(key="efilter", data=kwargs):
            _valid_efilters(efilters)

        datas = func(fgt_api, **kwargs)

        for efilter in efilters:
            efilter_by_sdst(policies=datas, efilter=efilter, rest=fgt_api.rest)
        return datas

    return wrapper


def efilter_by_sdst(policies: LDAny, efilter: str, rest) -> None:
    """Filter policies by efilter `srcaddr`, `dstaddr`.

    :param policies: Policies (side effect).
    :type policies: List[dict]

    :param str efilter: Extended filter.

    :param Fortigate rest: Fortigate REST API connector.

    :return: None. Updates policies (side effect). Pass policies matched by efilter.
    """
    if not _split_efilter(efilter)[0]:
        return
    # get addresses and address-groups from the Fortigate
    addresses: LDAny = Address(rest).get()
    addr_groups: LDAny = AddressGroup(rest).get()
    names_subnets_d: DLStr = _get_names_subnets(addresses, addr_groups)
    names_ipnets_d: DLInet = _convert_subnets_to_ipnets(names_subnets_d)

    # filter policies
    policies_ = _filter_policy_by_ipnets(efilter, policies, names_ipnets_d)
    policies.clear()
    policies.extend(policies_)


def _split_efilter(efilter: str) -> Tuple[str, str, IPv4Network]:
    """Parse `key`, `operator`, `value` from `efilter` for `srcaddr`, `dstaddr`.

    :param str efilter: Extended filter

    :return: efilter key, efilter operator, efilter value IPv4Network.
    """
    key, operator, value = vre.find3(pattern=r"(\w+)(..)(.+)", string=efilter)
    if key not in ["srcaddr", "dstaddr"]:
        return "", "", IPv4Network("0.0.0.0")
    ipnet = ip_network(value)
    if not isinstance(ipnet, IPv4Network):
        raise ValueError(f"{efilter=} {IPv4Network} expected")
    return key, operator, ipnet


def _get_names_subnets(addresses: LDAny, addr_groups: LDAny) -> DLStr:
    """Get all IPv4Networks from the Fortigate address-objects, address-group-objects.

    :param addresses: Fortigate address-objects.
    :param addr_groups: Fortigate address-group-objects.
    :return: Data indexed by address and address-group names (policy members).
    """
    members_d: DLStr = {d["name"]: [d["subnet"]] for d in addresses if d["type"] == "ipmask"}
    for addgr_d in addr_groups:
        addgr_name = addgr_d["name"]
        members_d[addgr_name] = []
    for addgr_d in addr_groups:
        addgr_name = addgr_d["name"]
        members_ = [d["name"] for d in addgr_d["member"]]
        for member_name in members_:
            subnets = members_d[member_name]
            members_d[addgr_name].extend(subnets)
    return members_d


def _convert_subnets_to_ipnets(members_d: DLStr) -> DLInet:
    """Convert subnets to IPv4Networks.

    :param members_d: Members names and subnets (in policies).

    :return: Members names and IPv4Networks.

    :example:
        members: {"ADDRESS": ["1.1.1.1 255.255.255.255"], "ADDR_GR": ["2.2.2.0 255.255.255.0"]}
        return: {"ADDRESS": [IPv4Network("1.1.1.1/32")], "ADDR_GR": [IPv4Network("2.2.2.0/24")]}
    """
    ipnets_d: DLInet = {}
    for name, subnets in members_d.items():
        ipnets_d[name] = []
    for name, subnets in members_d.items():
        for subnet in subnets:
            subnet = "/".join(subnet.strip().split(" "))
            try:
                ipnet = ip_network(subnet)
                if isinstance(ipnet, IPv4Network):
                    ipnets_d[name].append(ipnet)
            except ValueError as ex:
                msg = f"{type(ex).__name__}: {ex}"
                logging.error(msg)

    ipnets_d["all"] = [IPv4Network("0.0.0.0/0")]
    return ipnets_d


def _valid_efilters(efilters: LStr) -> None:
    """Validate efilters key, operator, value.

    :param efilters: Extended filters keys.
    :type efilters: List[str]

    :return: None. efilters has valid format.

    :raises ValueError: If efilter has invalid format.
    """
    re_operators = "|".join(EFILTER_OPERATORS)
    regex = fr"(\w+?)({re_operators})(.+)"
    keys: LStr = []
    for efilter in efilters:
        key, operator, _ = vre.find3(pattern=regex, string=efilter)
        keys.append(key)
        expected = EFILTER_KEYS
        if key not in expected:
            raise ValueError(f"invalid {efilter=}, {expected=}")
        expected = EFILTER_OPERATORS
        if operator not in expected:
            raise ValueError(f"invalid {operator=}, {expected=}")

    counts = Counter(keys)
    if invalid := [k for k, v in counts.items() if v > 1]:
        raise ValueError(f"{invalid=} in {efilters=}, expected only one key")


def _filter_policy_by_ipnets(efilter: str, policies: LDAny, names_ipnets_d: DLInet) -> LDAny:
    """Filter `policies` by `efilter` `srcaddr`, `dstaddr`.

    :param str efilter: Extended filter.
    :param policies: Policies.
    :param names_ipnets_d: Members names and IPv4Networks.
    :return: Filtered policies.
    """
    key, operator, ipnet_filter = _split_efilter(efilter)

    policies_: LDAny = []  # result
    for policy in policies:
        members = [d["name"] for d in policy[key]]
        for member in members:
            ipnets = names_ipnets_d.get(member)
            if not ipnets:
                msg = f"{member=} absent in ipnets"
                logging.error(msg)
                continue

            is_matched = False
            for ipnet in ipnets:
                if operator == "==":
                    if ipnet == ipnet_filter:
                        if policy not in policies_:
                            policies_.append(policy)
                elif operator == "<=":
                    if ipnet_filter.supernet_of(ipnet):
                        if policy not in policies_:
                            policies_.append(policy)
                elif operator == ">=":
                    if ipnet_filter.subnet_of(ipnet):
                        if policy not in policies_:
                            policies_.append(policy)
                elif operator == "!=":
                    if ipnet == ipnet_filter:
                        is_matched = False
                        break
                    if ipnet != ipnet_filter:
                        if policy not in policies_:
                            is_matched = True
            if operator == "!=" and is_matched is True:
                if policy not in policies_:
                    policies_.append(policy)
    return policies_
