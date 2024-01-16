"""Cmdb/firewall/interface-policy connector."""

from fortigate_api.connector import Connector


class InterfacePolicyFC(Connector):
    """Cmdb/firewall/interface-policy connector."""

    uid = "policyid"
    _path = "api/v2/cmdb/firewall/interface-policy"
