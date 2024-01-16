"""Cmdb/firewall/interface-policy6 connector."""

from fortigate_api.connector import Connector


class InterfacePolicy6FC(Connector):
    """Cmdb/firewall/interface-policy6 connector."""

    uid = "policyid"
    _path = "api/v2/cmdb/firewall/interface-policy6"
