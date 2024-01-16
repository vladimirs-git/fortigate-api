"""Cmdb/wireless-controller/wtp-profile connector."""

from fortigate_api.connector import Connector


class WtpProfileWcC(Connector):
    """Cmdb/wireless-controller/wtp-profile connector."""

    uid = "name"
    _path = "api/v2/cmdb/wireless-controller/wtp-profile"
