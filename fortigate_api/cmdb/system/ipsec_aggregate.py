"""Cmdb/system/ipsec-aggregate connector."""

from fortigate_api.connector import Connector


class IpsecAggregateSC(Connector):
    """Cmdb/system/ipsec-aggregate connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/ipsec-aggregate"
