"""Cmdb/system.lldp/network-policy connector."""

from fortigate_api.connector import Connector


class NetworkPolicySlC(Connector):
    """Cmdb/system.lldp/network-policy connector."""

    uid = "name"
    _path = "api/v2/cmdb/system.lldp/network-policy"
