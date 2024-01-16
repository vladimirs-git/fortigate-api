"""Cmdb/router/bgp connector."""

from fortigate_api.connector import Connector


class BgpRC(Connector):
    """Cmdb/router/bgp connector."""

    uid = ""
    _path = "api/v2/cmdb/router/bgp"
