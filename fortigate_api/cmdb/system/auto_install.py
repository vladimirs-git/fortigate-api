"""Cmdb/system/auto-install connector."""

from fortigate_api.connector import Connector


class AutoInstallSC(Connector):
    """Cmdb/system/auto-install connector."""

    uid = ""
    _path = "api/v2/cmdb/system/auto-install"
