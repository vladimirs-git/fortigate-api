"""Cmdb/router/route-map connector."""

from fortigate_api.connector import Connector


class RouteMapRC(Connector):
    """Cmdb/router/route-map connector."""

    uid = "name"
    _path = "api/v2/cmdb/router/route-map"
