"""Cmdb/user/peer connector."""

from fortigate_api.connector import Connector


class PeerUC(Connector):
    """Cmdb/user/peer connector."""

    uid = "name"
    _path = "api/v2/cmdb/user/peer"
