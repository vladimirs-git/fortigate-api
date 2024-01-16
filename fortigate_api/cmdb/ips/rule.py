"""Cmdb/ips/rule connector."""

from fortigate_api.connector import Connector


class RuleIC(Connector):
    """Cmdb/ips/rule connector."""

    uid = "name"
    _path = "api/v2/cmdb/ips/rule"
