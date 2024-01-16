"""Cmdb/firewall/central-snat-map connector."""

from fortigate_api.connector import Connector


class CentralSnatMapFC(Connector):
    """Cmdb/firewall/central-snat-map connector."""

    uid = "policyid"
    _path = "api/v2/cmdb/firewall/central-snat-map"
