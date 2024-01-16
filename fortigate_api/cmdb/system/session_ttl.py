"""Cmdb/system/session-ttl connector."""

from fortigate_api.connector import Connector


class SessionTtlSC(Connector):
    """Cmdb/system/session-ttl connector."""

    uid = ""
    _path = "api/v2/cmdb/system/session-ttl"
