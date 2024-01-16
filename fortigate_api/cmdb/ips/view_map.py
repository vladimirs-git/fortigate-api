"""Cmdb/ips/view-map connector."""

from fortigate_api.connector import Connector


class ViewMapIC(Connector):
    """Cmdb/ips/view-map connector."""

    uid = "id"
    _path = "api/v2/cmdb/ips/view-map"
