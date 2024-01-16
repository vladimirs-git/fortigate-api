"""Cmdb/user/fsso connector."""

from fortigate_api.connector import Connector


class FssoUC(Connector):
    """Cmdb/user/fsso connector."""

    uid = "name"
    _path = "api/v2/cmdb/user/fsso"
