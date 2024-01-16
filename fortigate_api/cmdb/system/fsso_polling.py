"""Cmdb/system/fsso-polling connector."""

from fortigate_api.connector import Connector


class FssoPollingSC(Connector):
    """Cmdb/system/fsso-polling connector."""

    uid = ""
    _path = "api/v2/cmdb/system/fsso-polling"
