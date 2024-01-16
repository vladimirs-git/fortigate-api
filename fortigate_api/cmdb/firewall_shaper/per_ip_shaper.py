"""Cmdb/firewall.shaper/per-ip-shaper connector."""

from fortigate_api.connector import Connector


class PerIpShaperFsC(Connector):
    """Cmdb/firewall.shaper/per-ip-shaper connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall.shaper/per-ip-shaper"
