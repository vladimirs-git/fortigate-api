"""Cmdb/router/key-chain connector."""

from fortigate_api.connector import Connector


class KeyChainRC(Connector):
    """Cmdb/router/key-chain connector."""

    uid = "name"
    _path = "api/v2/cmdb/router/key-chain"
