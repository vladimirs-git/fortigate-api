"""Cmdb/system/vdom-property connector."""

from fortigate_api.connector import Connector


class VdomPropertySC(Connector):
    """Cmdb/system/vdom-property connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/vdom-property"
