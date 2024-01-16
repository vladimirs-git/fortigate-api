"""Cmdb/firewall.ipmacbinding/table connector."""

from fortigate_api.connector import Connector


class TableFiC(Connector):
    """Cmdb/firewall.ipmacbinding/table connector."""

    uid = "seq-num"
    _path = "api/v2/cmdb/firewall.ipmacbinding/table"
