"""Cmdb/firewall/local-in-policy connector."""

from fortigate_api.connector import Connector


class LocalInPolicyFC(Connector):
    """Cmdb/firewall/local-in-policy connector."""

    uid = "policyid"
    _path = "api/v2/cmdb/firewall/local-in-policy"
