"""Cmdb/system/mac-address-table connector."""

from fortigate_api.connector import Connector


class MacAddressTableSC(Connector):
    """Cmdb/system/mac-address-table connector."""

    uid = "mac"
    _path = "api/v2/cmdb/system/mac-address-table"
