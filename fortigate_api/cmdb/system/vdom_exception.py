"""Cmdb/system/vdom-exception connector."""

from fortigate_api.connector import Connector


class VdomExceptionSC(Connector):
    """Cmdb/system/vdom-exception connector."""

    uid = "id"
    _path = "api/v2/cmdb/system/vdom-exception"
