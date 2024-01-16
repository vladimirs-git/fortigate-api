"""Cmdb/firewall/security-policy connector."""

from fortigate_api.connector import Connector


class SecurityPolicyFC(Connector):
    """Cmdb/firewall/security-policy connector."""

    uid = "policyid"
    _path = "api/v2/cmdb/firewall/security-policy"
