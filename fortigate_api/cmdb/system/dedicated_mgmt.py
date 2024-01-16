"""Cmdb/system/dedicated-mgmt connector."""

from fortigate_api.connector import Connector


class DedicatedMgmtSC(Connector):
    """Cmdb/system/dedicated-mgmt connector."""

    uid = ""
    _path = "api/v2/cmdb/system/dedicated-mgmt"
