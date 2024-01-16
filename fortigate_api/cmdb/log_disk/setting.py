"""Cmdb/log.disk/setting connector."""

from fortigate_api.connector import Connector


class SettingLdC(Connector):
    """Cmdb/log.disk/setting connector."""

    uid = ""
    _path = "api/v2/cmdb/log.disk/setting"
