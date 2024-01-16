"""Cmdb/dlp/sensitivity connector."""

from fortigate_api.connector import Connector


class SensitivityDC(Connector):
    """Cmdb/dlp/sensitivity connector."""

    uid = "name"
    _path = "api/v2/cmdb/dlp/sensitivity"
