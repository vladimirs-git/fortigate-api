"""Cmdb/wireless-controller/timers connector."""

from fortigate_api.connector import Connector


class TimersWcC(Connector):
    """Cmdb/wireless-controller/timers connector."""

    uid = ""
    _path = "api/v2/cmdb/wireless-controller/timers"
