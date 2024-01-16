"""Cmdb/system/sdwan connector."""

from fortigate_api.connector import Connector


class SdwanSC(Connector):
    """Cmdb/system/sdwan connector."""

    uid = ""
    _path = "api/v2/cmdb/system/sdwan"
