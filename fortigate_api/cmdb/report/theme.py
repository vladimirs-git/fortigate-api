"""Cmdb/report/theme connector."""

from fortigate_api.connector import Connector


class ThemeRC(Connector):
    """Cmdb/report/theme connector."""

    uid = "name"
    _path = "api/v2/cmdb/report/theme"
