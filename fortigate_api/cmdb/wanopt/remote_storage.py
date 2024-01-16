"""Cmdb/wanopt/remote-storage connector."""

from fortigate_api.connector import Connector


class RemoteStorageWC(Connector):
    """Cmdb/wanopt/remote-storage connector."""

    uid = ""
    _path = "api/v2/cmdb/wanopt/remote-storage"
