"""Cmdb/switch-controller/nac-device connector."""

from fortigate_api.connector import Connector


class NacDeviceScC(Connector):
    """Cmdb/switch-controller/nac-device connector."""

    uid = "id"
    _path = "api/v2/cmdb/switch-controller/nac-device"
