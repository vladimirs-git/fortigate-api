"""Cmdb/firewall/policy64 connector."""

from fortigate_api.connector import Connector


class Policy64FC(Connector):
    """Cmdb/firewall/policy64 connector."""

    uid = "policyid"
    _path = "api/v2/cmdb/firewall/policy64"
