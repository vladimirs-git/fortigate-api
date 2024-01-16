"""Cmdb/wireless-controller/arrp-profile connector."""

from fortigate_api.connector import Connector


class ArrpProfileWcC(Connector):
    """Cmdb/wireless-controller/arrp-profile connector."""

    uid = "name"
    _path = "api/v2/cmdb/wireless-controller/arrp-profile"
