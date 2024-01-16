"""Cmdb/system/alarm connector."""

from fortigate_api.connector import Connector


class AlarmSC(Connector):
    """Cmdb/system/alarm connector."""

    uid = ""
    _path = "api/v2/cmdb/system/alarm"
