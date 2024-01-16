"""Cmdb/router/isis connector."""

from fortigate_api.connector import Connector


class IsisRC(Connector):
    """Cmdb/router/isis connector."""

    uid = ""
    _path = "api/v2/cmdb/router/isis"
