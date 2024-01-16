"""Cmdb/ips/custom connector."""

from fortigate_api.connector import Connector


class CustomIC(Connector):
    """Cmdb/ips/custom connector."""

    uid = "tag"
    _path = "api/v2/cmdb/ips/custom"
