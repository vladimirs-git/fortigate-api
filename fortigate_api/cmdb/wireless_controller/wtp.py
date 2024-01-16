"""Cmdb/wireless-controller/wtp connector."""

from fortigate_api.connector import Connector


class WtpWcC(Connector):
    """Cmdb/wireless-controller/wtp connector."""

    uid = "wtp-id"
    _path = "api/v2/cmdb/wireless-controller/wtp"
