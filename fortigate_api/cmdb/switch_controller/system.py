"""Cmdb/switch-controller/system connector."""

from fortigate_api.connector import Connector


class SystemScC(Connector):
    """Cmdb/switch-controller/system connector."""

    uid = ""
    _path = "api/v2/cmdb/switch-controller/system"
