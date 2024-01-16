"""Cmdb/system/ips-urlfilter-dns connector."""

from fortigate_api.connector import Connector


class IpsUrlfilterDnsSC(Connector):
    """Cmdb/system/ips-urlfilter-dns connector."""

    uid = "address"
    _path = "api/v2/cmdb/system/ips-urlfilter-dns"
