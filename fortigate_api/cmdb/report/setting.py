"""Cmdb/report/setting connector."""

from fortigate_api.connector import Connector


class SettingRC(Connector):
    """Cmdb/report/setting connector."""

    uid = ""
    _path = "api/v2/cmdb/report/setting"
