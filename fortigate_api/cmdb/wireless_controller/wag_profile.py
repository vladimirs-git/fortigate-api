"""Cmdb/wireless-controller/wag-profile connector."""

from fortigate_api.connector import Connector


class WagProfileWcC(Connector):
    """Cmdb/wireless-controller/wag-profile connector."""

    uid = "name"
    _path = "api/v2/cmdb/wireless-controller/wag-profile"
