"""Cmdb/dnsfilter connectors."""

from fortigate_api.cmdb.dnsfilter.domain_filter import DomainFilterDC
from fortigate_api.cmdb.dnsfilter.profile import ProfileDC
from fortigate_api.fortigate import FortiGate


class DnsfilterC:
    """Cmdb/dnsfilter connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init DnsfilterC."""
        self.domain_filter = DomainFilterDC(fortigate, **kwargs)
        """:py:class:`.DomainFilterDC` cmdb/dnsfilter/domain-filter."""

        self.profile = ProfileDC(fortigate, **kwargs)
        """:py:class:`.ProfileDC` cmdb/dnsfilter/profile."""
