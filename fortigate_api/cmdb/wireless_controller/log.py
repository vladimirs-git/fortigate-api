"""Cmdb/wireless-controller/log connector."""

from fortigate_api.connector import Connector


class LogWcC(Connector):
    """Cmdb/wireless-controller/log connector."""

    uid = ""
    _path = "api/v2/cmdb/wireless-controller/log"
