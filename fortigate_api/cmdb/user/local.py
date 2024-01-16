"""Cmdb/user/local connector."""

from fortigate_api.connector import Connector


class LocalUC(Connector):
    """Cmdb/user/local connector."""

    uid = "name"
    _path = "api/v2/cmdb/user/local"
