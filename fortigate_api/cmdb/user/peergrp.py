"""Cmdb/user/peergrp connector."""

from fortigate_api.connector import Connector


class PeergrpUC(Connector):
    """Cmdb/user/peergrp connector."""

    uid = "name"
    _path = "api/v2/cmdb/user/peergrp"
