"""Cmdb/system/fortimanager connector."""

from fortigate_api.connector import Connector


class FortimanagerSC(Connector):
    """Cmdb/system/fortimanager connector."""

    uid = ""
    _path = "api/v2/cmdb/system/fortimanager"
