"""Cmdb/system/npu connector."""

from fortigate_api.connector import Connector


class NpuSC(Connector):
    """Cmdb/system/npu connector."""

    uid = ""
    _path = "api/v2/cmdb/system/npu"
