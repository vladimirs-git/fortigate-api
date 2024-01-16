"""Cmdb/wireless-controller/utm-profile connector."""

from fortigate_api.connector import Connector


class UtmProfileWcC(Connector):
    """Cmdb/wireless-controller/utm-profile connector."""

    uid = "name"
    _path = "api/v2/cmdb/wireless-controller/utm-profile"
