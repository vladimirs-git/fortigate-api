"""Cmdb/system/probe-response connector."""

from fortigate_api.connector import Connector


class ProbeResponseSC(Connector):
    """Cmdb/system/probe-response connector."""

    uid = ""
    _path = "api/v2/cmdb/system/probe-response"
