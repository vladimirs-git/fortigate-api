"""Cmdb/firewall/policy46 connector."""

from fortigate_api.connector import Connector


class Policy46FC(Connector):
    """Cmdb/firewall/policy46 connector."""

    uid = "policyid"
    _path = "api/v2/cmdb/firewall/policy46"
