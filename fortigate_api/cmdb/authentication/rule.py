"""Cmdb/authentication/rule connector."""

from fortigate_api.connector import Connector


class RuleAC(Connector):
    """Cmdb/authentication/rule connector."""

    uid = "name"
    _path = "api/v2/cmdb/authentication/rule"
