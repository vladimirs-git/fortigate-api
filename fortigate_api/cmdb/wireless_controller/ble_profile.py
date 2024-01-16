"""Cmdb/wireless-controller/ble-profile connector."""

from fortigate_api.connector import Connector


class BleProfileWcC(Connector):
    """Cmdb/wireless-controller/ble-profile connector."""

    uid = "name"
    _path = "api/v2/cmdb/wireless-controller/ble-profile"
