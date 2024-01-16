"""Cmdb/router/setting connector."""

from fortigate_api.connector import Connector


class SettingRC(Connector):
    """Cmdb/router/setting connector."""

    uid = ""
    _path = "api/v2/cmdb/router/setting"
