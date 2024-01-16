"""Cmdb/router/access-list connector."""

from fortigate_api.connector import Connector


class AccessListRC(Connector):
    """Cmdb/router/access-list connector."""

    uid = "name"
    _path = "api/v2/cmdb/router/access-list"
