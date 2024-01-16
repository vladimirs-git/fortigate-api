"""Cmdb/alertemail/setting connector."""

from fortigate_api.connector import Connector


class SettingAC(Connector):
    """Cmdb/alertemail/setting connector."""

    uid = ""
    _path = "api/v2/cmdb/alertemail/setting"
