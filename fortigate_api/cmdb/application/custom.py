"""Cmdb/application/custom connector."""

from fortigate_api.connector import Connector


class CustomAC(Connector):
    """Cmdb/application/custom connector."""

    uid = "tag"
    _path = "api/v2/cmdb/application/custom"
