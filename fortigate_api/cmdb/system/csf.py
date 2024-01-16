"""Cmdb/system/csf connector."""

from fortigate_api.connector import Connector


class CsfSC(Connector):
    """Cmdb/system/csf connector."""

    uid = ""
    _path = "api/v2/cmdb/system/csf"
