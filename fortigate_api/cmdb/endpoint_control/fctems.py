"""Cmdb/endpoint-control/fctems connector."""

from fortigate_api.connector import Connector


class FctemsEcC(Connector):
    """Cmdb/endpoint-control/fctems connector."""

    uid = "name"
    _path = "api/v2/cmdb/endpoint-control/fctems"
