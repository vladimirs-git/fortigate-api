"""Cmdb/wireless-controller/bonjour-profile connector."""

from fortigate_api.connector import Connector


class BonjourProfileWcC(Connector):
    """Cmdb/wireless-controller/bonjour-profile connector."""

    uid = "name"
    _path = "api/v2/cmdb/wireless-controller/bonjour-profile"
