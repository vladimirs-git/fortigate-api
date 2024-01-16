"""Cmdb/system/nat64 connector."""

from fortigate_api.connector import Connector


class Nat64SC(Connector):
    """Cmdb/system/nat64 connector."""

    uid = ""
    _path = "api/v2/cmdb/system/nat64"
