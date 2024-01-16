"""Cmdb/wireless-controller/wids-profile connector."""

from fortigate_api.connector import Connector


class WidsProfileWcC(Connector):
    """Cmdb/wireless-controller/wids-profile connector."""

    uid = "name"
    _path = "api/v2/cmdb/wireless-controller/wids-profile"
