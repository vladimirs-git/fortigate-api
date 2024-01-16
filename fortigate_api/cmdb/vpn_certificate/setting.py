"""Cmdb/vpn.certificate/setting connector."""

from fortigate_api.connector import Connector


class SettingVcC(Connector):
    """Cmdb/vpn.certificate/setting connector."""

    uid = ""
    _path = "api/v2/cmdb/vpn.certificate/setting"
