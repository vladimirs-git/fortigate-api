"""Cmdb/report/layout connector."""

from fortigate_api.connector import Connector


class LayoutRC(Connector):
    """Cmdb/report/layout connector."""

    uid = "name"
    _path = "api/v2/cmdb/report/layout"
