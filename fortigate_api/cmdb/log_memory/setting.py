"""Cmdb/log.memory/setting connector."""

from fortigate_api.connector import Connector


class SettingLmC(Connector):
    """Cmdb/log.memory/setting connector."""

    uid = ""
    _path = "api/v2/cmdb/log.memory/setting"
