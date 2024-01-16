"""Cmdb/wireless-controller/wtp-group connector."""

from fortigate_api.connector import Connector


class WtpGroupWcC(Connector):
    """Cmdb/wireless-controller/wtp-group connector."""

    uid = "name"
    _path = "api/v2/cmdb/wireless-controller/wtp-group"
