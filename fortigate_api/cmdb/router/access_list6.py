"""Cmdb/router/access-list6 connector."""

from fortigate_api.connector import Connector


class AccessList6RC(Connector):
    """Cmdb/router/access-list6 connector."""

    uid = "name"
    _path = "api/v2/cmdb/router/access-list6"
