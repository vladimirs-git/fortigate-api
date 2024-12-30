"""Cmdb/firewall.shaper connectors."""

from fortigate_api.cmdb.firewall_shaper.per_ip_shaper import PerIpShaperFsC
from fortigate_api.cmdb.firewall_shaper.traffic_shaper import TrafficShaperFsC
from fortigate_api.fortigate import FortiGate


class FirewallShaperC:
    """Cmdb/firewall.shaper connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init FirewallShaperC."""
        self.per_ip_shaper = PerIpShaperFsC(fortigate, **kwargs)
        """:py:class:`.PerIpShaperFsC` cmdb/firewall.shaper/per-ip-shaper."""

        self.traffic_shaper = TrafficShaperFsC(fortigate, **kwargs)
        """:py:class:`.TrafficShaperFsC` cmdb/firewall.shaper/traffic-shaper."""
