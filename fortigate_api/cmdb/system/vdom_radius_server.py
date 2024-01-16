"""Cmdb/system/vdom-radius-server connector."""

from fortigate_api.connector import Connector


class VdomRadiusServerSC(Connector):
    """Cmdb/system/vdom-radius-server connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/vdom-radius-server"
