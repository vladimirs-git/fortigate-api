"""Cmdb/router/aspath-list connector."""

from fortigate_api.connector import Connector


class AspathListRC(Connector):
    """Cmdb/router/aspath-list connector."""

    uid = "name"
    _path = "api/v2/cmdb/router/aspath-list"
