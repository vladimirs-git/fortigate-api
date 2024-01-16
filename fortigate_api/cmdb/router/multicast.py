"""Cmdb/router/multicast connector."""

from fortigate_api.connector import Connector


class MulticastRC(Connector):
    """Cmdb/router/multicast connector."""

    uid = ""
    _path = "api/v2/cmdb/router/multicast"
