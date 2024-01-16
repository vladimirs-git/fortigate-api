"""Cmdb/log.fortiguard/setting connector."""

from fortigate_api.connector import Connector


class SettingLfC(Connector):
    """Cmdb/log.fortiguard/setting connector."""

    uid = ""
    _path = "api/v2/cmdb/log.fortiguard/setting"
