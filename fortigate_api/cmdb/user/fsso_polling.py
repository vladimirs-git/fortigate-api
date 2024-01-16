"""Cmdb/user/fsso-polling connector."""

from fortigate_api.connector import Connector


class FssoPollingUC(Connector):
    """Cmdb/user/fsso-polling connector."""

    uid = "id"
    _path = "api/v2/cmdb/user/fsso-polling"
