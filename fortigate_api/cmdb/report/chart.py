"""Cmdb/report/chart connector."""

from fortigate_api.connector import Connector


class ChartRC(Connector):
    """Cmdb/report/chart connector."""

    uid = "name"
    _path = "api/v2/cmdb/report/chart"
