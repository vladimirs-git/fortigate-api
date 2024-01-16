"""Cmdb/system/session-helper connector."""

from fortigate_api.connector import Connector


class SessionHelperSC(Connector):
    """Cmdb/system/session-helper connector."""

    uid = "id"
    _path = "api/v2/cmdb/system/session-helper"
