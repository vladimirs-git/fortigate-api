"""Cmdb/system/sflow connector."""

from fortigate_api.connector import Connector


class SflowSC(Connector):
    """Cmdb/system/sflow connector."""

    uid = ""
    _path = "api/v2/cmdb/system/sflow"
