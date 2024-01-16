"""Cmdb/router/static connector."""

from fortigate_api.connector import Connector


class StaticRC(Connector):
    """Cmdb/router/static connector."""

    uid = "seq-num"
    _path = "api/v2/cmdb/router/static"
