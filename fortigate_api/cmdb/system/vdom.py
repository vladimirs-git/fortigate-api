"""Cmdb/system/vdom connector."""

from fortigate_api.connector import Connector


class VdomSC(Connector):
    """Cmdb/system/vdom connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/vdom"
    _path_ui = "ng/system/vdom"
