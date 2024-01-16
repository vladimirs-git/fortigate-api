"""Cmdb/report/dataset connector."""

from fortigate_api.connector import Connector


class DatasetRC(Connector):
    """Cmdb/report/dataset connector."""

    uid = "name"
    _path = "api/v2/cmdb/report/dataset"
