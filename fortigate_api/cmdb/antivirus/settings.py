"""Cmdb/antivirus/settings connector."""

from fortigate_api.connector import Connector


class SettingsAC(Connector):
    """Cmdb/antivirus/settings connector."""

    uid = ""
    _path = "api/v2/cmdb/antivirus/settings"
