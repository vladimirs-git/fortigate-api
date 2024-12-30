"""Cmdb/router connectors."""

from fortigate_api.cmdb.router.access_list import AccessListRC
from fortigate_api.cmdb.router.access_list6 import AccessList6RC
from fortigate_api.cmdb.router.aspath_list import AspathListRC
from fortigate_api.cmdb.router.auth_path import AuthPathRC
from fortigate_api.cmdb.router.bfd import BfdRC
from fortigate_api.cmdb.router.bfd6 import Bfd6RC
from fortigate_api.cmdb.router.bgp import BgpRC
from fortigate_api.cmdb.router.community_list import CommunityListRC
from fortigate_api.cmdb.router.isis import IsisRC
from fortigate_api.cmdb.router.key_chain import KeyChainRC
from fortigate_api.cmdb.router.multicast import MulticastRC
from fortigate_api.cmdb.router.multicast6 import Multicast6RC
from fortigate_api.cmdb.router.multicast_flow import MulticastFlowRC
from fortigate_api.cmdb.router.ospf import OspfRC
from fortigate_api.cmdb.router.ospf6 import Ospf6RC
from fortigate_api.cmdb.router.policy import PolicyRC
from fortigate_api.cmdb.router.policy6 import Policy6RC
from fortigate_api.cmdb.router.prefix_list import PrefixListRC
from fortigate_api.cmdb.router.prefix_list6 import PrefixList6RC
from fortigate_api.cmdb.router.rip import RipRC
from fortigate_api.cmdb.router.ripng import RipngRC
from fortigate_api.cmdb.router.route_map import RouteMapRC
from fortigate_api.cmdb.router.setting import SettingRC
from fortigate_api.cmdb.router.static import StaticRC
from fortigate_api.cmdb.router.static6 import Static6RC
from fortigate_api.fortigate import FortiGate


class RouterC:
    """Cmdb/router connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init RouterC."""
        self.access_list = AccessListRC(fortigate, **kwargs)
        """:py:class:`.AccessListRC` cmdb/router/access-list."""

        self.access_list6 = AccessList6RC(fortigate, **kwargs)
        """:py:class:`.AccessList6RC` cmdb/router/access-list6."""

        self.aspath_list = AspathListRC(fortigate, **kwargs)
        """:py:class:`.AspathListRC` cmdb/router/aspath-list."""

        self.auth_path = AuthPathRC(fortigate, **kwargs)
        """:py:class:`.AuthPathRC` cmdb/router/auth-path."""

        self.bfd = BfdRC(fortigate, **kwargs)
        """:py:class:`.BfdRC` cmdb/router/bfd."""

        self.bfd6 = Bfd6RC(fortigate, **kwargs)
        """:py:class:`.Bfd6RC` cmdb/router/bfd6."""

        self.bgp = BgpRC(fortigate, **kwargs)
        """:py:class:`.BgpRC` cmdb/router/bgp."""

        self.community_list = CommunityListRC(fortigate, **kwargs)
        """:py:class:`.CommunityListRC` cmdb/router/community-list."""

        self.isis = IsisRC(fortigate, **kwargs)
        """:py:class:`.IsisRC` cmdb/router/isis."""

        self.key_chain = KeyChainRC(fortigate, **kwargs)
        """:py:class:`.KeyChainRC` cmdb/router/key-chain."""

        self.multicast = MulticastRC(fortigate, **kwargs)
        """:py:class:`.MulticastRC` cmdb/router/multicast."""

        self.multicast_flow = MulticastFlowRC(fortigate, **kwargs)
        """:py:class:`.MulticastFlowRC` cmdb/router/multicast-flow."""

        self.multicast6 = Multicast6RC(fortigate, **kwargs)
        """:py:class:`.Multicast6RC` cmdb/router/multicast6."""

        self.ospf = OspfRC(fortigate, **kwargs)
        """:py:class:`.OspfRC` cmdb/router/ospf."""

        self.ospf6 = Ospf6RC(fortigate, **kwargs)
        """:py:class:`.Ospf6RC` cmdb/router/ospf6."""

        self.policy = PolicyRC(fortigate, **kwargs)
        """:py:class:`.PolicyRC` cmdb/router/policy."""

        self.policy6 = Policy6RC(fortigate, **kwargs)
        """:py:class:`.Policy6RC` cmdb/router/policy6."""

        self.prefix_list = PrefixListRC(fortigate, **kwargs)
        """:py:class:`.PrefixListRC` cmdb/router/prefix-list."""

        self.prefix_list6 = PrefixList6RC(fortigate, **kwargs)
        """:py:class:`.PrefixList6RC` cmdb/router/prefix-list6."""

        self.rip = RipRC(fortigate, **kwargs)
        """:py:class:`.RipRC` cmdb/router/rip."""

        self.ripng = RipngRC(fortigate, **kwargs)
        """:py:class:`.RipngRC` cmdb/router/ripng."""

        self.route_map = RouteMapRC(fortigate, **kwargs)
        """:py:class:`.RouteMapRC` cmdb/router/route-map."""

        self.setting = SettingRC(fortigate, **kwargs)
        """:py:class:`.SettingRC` cmdb/router/setting."""

        self.static = StaticRC(fortigate, **kwargs)
        """:py:class:`.StaticRC` cmdb/router/static."""

        self.static6 = Static6RC(fortigate, **kwargs)
        """:py:class:`.Static6RC` cmdb/router/static6."""
