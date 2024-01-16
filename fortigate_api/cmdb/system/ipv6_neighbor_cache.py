"""Cmdb/system/ipv6-neighbor-cache connector."""

from fortigate_api.connector import Connector


class Ipv6NeighborCacheSC(Connector):
    """Cmdb/system/ipv6-neighbor-cache connector."""

    uid = "id"
    _path = "api/v2/cmdb/system/ipv6-neighbor-cache"
