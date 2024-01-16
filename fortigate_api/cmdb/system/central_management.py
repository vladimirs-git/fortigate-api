"""Cmdb/system/central-management connector."""

from fortigate_api.connector import Connector


class CentralManagementSC(Connector):
    """Cmdb/system/central-management connector."""

    uid = ""
    _path = "api/v2/cmdb/system/central-management"
