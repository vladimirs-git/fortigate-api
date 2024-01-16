"""Cmdb/system/arp-table connector."""

from fortigate_api.connector import Connector


class ArpTableSC(Connector):
    """Cmdb/system/arp-table connector."""

    uid = "id"
    _path = "api/v2/cmdb/system/arp-table"
