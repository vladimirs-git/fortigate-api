"""Cmdb/wanopt/peer connector."""

from fortigate_api.connector import Connector


class PeerWC(Connector):
    """Cmdb/wanopt/peer connector."""

    uid = "peer-host-id"
    _path = "api/v2/cmdb/wanopt/peer"
