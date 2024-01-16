"""Cmdb/firewall/country connector."""

from fortigate_api.connector import Connector


class CountryFC(Connector):
    """Cmdb/firewall/country connector."""

    uid = "id"
    _path = "api/v2/cmdb/firewall/country"
