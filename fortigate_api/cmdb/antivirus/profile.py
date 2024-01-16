"""Cmdb/antivirus/profile connector."""

from fortigate_api.connector import Connector


class ProfileAC(Connector):
    """Cmdb/antivirus/profile connector."""

    uid = "name"
    _path = "api/v2/cmdb/antivirus/profile"
    _path_ui = "ng/utm/antivirus/profile"
