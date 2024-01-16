"""Cmdb/firewall.ssh/setting connector."""

from fortigate_api.connector import Connector


class SettingFsC(Connector):
    """Cmdb/firewall.ssh/setting connector."""

    uid = ""
    _path = "api/v2/cmdb/firewall.ssh/setting"
