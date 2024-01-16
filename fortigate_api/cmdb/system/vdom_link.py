"""Cmdb/system/vdom-link connector."""

from fortigate_api.connector import Connector


class VdomLinkSC(Connector):
    """Cmdb/system/vdom-link connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/vdom-link"
