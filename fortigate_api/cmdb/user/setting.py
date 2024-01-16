"""Cmdb/user/setting connector."""

from fortigate_api.connector import Connector


class SettingUC(Connector):
    """Cmdb/user/setting connector."""

    uid = ""
    _path = "api/v2/cmdb/user/setting"
