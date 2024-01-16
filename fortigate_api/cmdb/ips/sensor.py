"""Cmdb/ips/sensor connector."""

from fortigate_api.connector import Connector


class SensorIC(Connector):
    """Cmdb/ips/sensor connector."""

    uid = "name"
    _path = "api/v2/cmdb/ips/sensor"
