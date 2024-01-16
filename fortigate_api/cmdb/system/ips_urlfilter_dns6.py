"""Cmdb/system/ips-urlfilter-dns6 connector."""

from fortigate_api.connector import Connector


class IpsUrlfilterDns6SC(Connector):
    """Cmdb/system/ips-urlfilter-dns6 connector."""

    uid = "address6"
    _path = "api/v2/cmdb/system/ips-urlfilter-dns6"
