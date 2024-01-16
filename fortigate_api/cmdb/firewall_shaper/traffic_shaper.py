"""Cmdb/firewall.shaper/traffic-shaper connector."""

from fortigate_api.connector import Connector


class TrafficShaperFsC(Connector):
    """Cmdb/firewall.shaper/traffic-shaper connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall.shaper/traffic-shaper"
