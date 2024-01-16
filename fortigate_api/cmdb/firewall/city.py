"""Cmdb/firewall/city connector."""

from fortigate_api.connector import Connector


class CityFC(Connector):
    """Cmdb/firewall/city connector."""

    uid = "id"
    _path = "api/v2/cmdb/firewall/city"
