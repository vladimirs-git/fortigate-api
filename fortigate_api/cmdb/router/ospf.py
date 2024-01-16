"""Cmdb/router/ospf connector."""

from fortigate_api.connector import Connector


class OspfRC(Connector):
    """Cmdb/router/ospf connector."""

    uid = ""
    _path = "api/v2/cmdb/router/ospf"
