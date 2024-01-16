"""Cmdb/firewall/region connector."""

from fortigate_api.connector import Connector


class RegionFC(Connector):
    """Cmdb/firewall/region connector."""

    uid = "id"
    _path = "api/v2/cmdb/firewall/region"
