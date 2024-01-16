"""Cmdb/firewall.ssl/setting connector."""

from fortigate_api.connector import Connector


class SettingFsC(Connector):
    """Cmdb/firewall.ssl/setting connector."""

    uid = ""
    _path = "api/v2/cmdb/firewall.ssl/setting"
