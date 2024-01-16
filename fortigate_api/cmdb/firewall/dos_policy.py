"""Cmdb/firewall/dos-policy connector."""

from fortigate_api.connector import Connector


class DosPolicyFC(Connector):
    """Cmdb/firewall/dos-policy connector."""

    uid = "policyid"
    _path = "api/v2/cmdb/firewall/DoS-policy"
