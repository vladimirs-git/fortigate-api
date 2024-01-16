"""Cmdb/wireless-controller/inter-controller connector."""

from fortigate_api.connector import Connector


class InterControllerWcC(Connector):
    """Cmdb/wireless-controller/inter-controller connector."""

    uid = ""
    _path = "api/v2/cmdb/wireless-controller/inter-controller"
