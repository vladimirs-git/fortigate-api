"""Cmdb/wireless-controller/mpsk-profile connector."""

from fortigate_api.connector import Connector


class MpskProfileWcC(Connector):
    """Cmdb/wireless-controller/mpsk-profile connector."""

    uid = "name"
    _path = "api/v2/cmdb/wireless-controller/mpsk-profile"
