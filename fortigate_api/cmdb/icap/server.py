"""Cmdb/icap/server connector."""

from fortigate_api.connector import Connector


class ServerIC(Connector):
    """Cmdb/icap/server connector."""

    uid = "name"
    _path = "api/v2/cmdb/icap/server"
