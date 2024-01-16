"""Cmdb/report/style connector."""

from fortigate_api.connector import Connector


class StyleRC(Connector):
    """Cmdb/report/style connector."""

    uid = "name"
    _path = "api/v2/cmdb/report/style"
