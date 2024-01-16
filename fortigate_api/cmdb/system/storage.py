"""Cmdb/system/storage connector."""

from fortigate_api.connector import Connector


class StorageSC(Connector):
    """Cmdb/system/storage connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/storage"
