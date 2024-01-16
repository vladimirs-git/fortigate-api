"""Cmdb/dlp/sensor connector."""

from fortigate_api.connector import Connector


class SensorDC(Connector):
    """Cmdb/dlp/sensor connector."""

    uid = "name"
    _path = "api/v2/cmdb/dlp/sensor"
