"""Cmdb/firewall/proxy-policy connector."""

from fortigate_api.connector import Connector


class ProxyPolicyFC(Connector):
    """Cmdb/firewall/proxy-policy connector."""

    uid = "policyid"
    _path = "api/v2/cmdb/firewall/proxy-policy"
