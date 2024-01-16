"""Cmdb/log/gui-display connector."""

from fortigate_api.connector import Connector


class GuiDisplayLC(Connector):
    """Cmdb/log/gui-display connector."""

    uid = ""
    _path = "api/v2/cmdb/log/gui-display"
