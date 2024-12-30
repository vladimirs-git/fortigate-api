"""Cmdb/emailfilter connectors."""

from fortigate_api.cmdb.emailfilter.bwl import BwlEC
from fortigate_api.cmdb.emailfilter.bword import BwordEC
from fortigate_api.cmdb.emailfilter.dnsbl import DnsblEC
from fortigate_api.cmdb.emailfilter.fortishield import FortishieldEC
from fortigate_api.cmdb.emailfilter.iptrust import IptrustEC
from fortigate_api.cmdb.emailfilter.mheader import MheaderEC
from fortigate_api.cmdb.emailfilter.options import OptionsEC
from fortigate_api.cmdb.emailfilter.profile import ProfileEC
from fortigate_api.fortigate import FortiGate


class EmailfilterC:
    """Cmdb/emailfilter connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init EmailfilterC."""
        self.bwl = BwlEC(fortigate, **kwargs)
        """:py:class:`.BwlEC` cmdb/emailfilter/bwl."""

        self.bword = BwordEC(fortigate, **kwargs)
        """:py:class:`.BwordEC` cmdb/emailfilter/bword."""

        self.dnsbl = DnsblEC(fortigate, **kwargs)
        """:py:class:`.DnsblEC` cmdb/emailfilter/dnsbl."""

        self.fortishield = FortishieldEC(fortigate, **kwargs)
        """:py:class:`.FortishieldEC` cmdb/emailfilter/fortishield."""

        self.iptrust = IptrustEC(fortigate, **kwargs)
        """:py:class:`.IptrustEC` cmdb/emailfilter/iptrust."""

        self.mheader = MheaderEC(fortigate, **kwargs)
        """:py:class:`.MheaderEC` cmdb/emailfilter/mheader."""

        self.options = OptionsEC(fortigate, **kwargs)
        """:py:class:`.OptionsEC` cmdb/emailfilter/options."""

        self.profile = ProfileEC(fortigate, **kwargs)
        """:py:class:`.ProfileEC` cmdb/emailfilter/profile."""
