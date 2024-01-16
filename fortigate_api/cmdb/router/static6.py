"""Cmdb/router/static6 connector."""

from fortigate_api.connector import Connector


class Static6RC(Connector):
    """Cmdb/router/static6 connector."""

    uid = "seq-num"
    _path = "api/v2/cmdb/router/static6"
