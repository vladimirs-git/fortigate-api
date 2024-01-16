"""Cmdb/switch-controller/location connector."""

from fortigate_api.connector import Connector


class LocationScC(Connector):
    """Cmdb/switch-controller/location connector."""

    uid = "name"
    _path = "api/v2/cmdb/switch-controller/location"
