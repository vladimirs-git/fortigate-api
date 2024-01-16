"""Cmdb/router/ospf6 connector."""

from fortigate_api.connector import Connector


class Ospf6RC(Connector):
    """Cmdb/router/ospf6 connector."""

    uid = ""
    _path = "api/v2/cmdb/router/ospf6"
