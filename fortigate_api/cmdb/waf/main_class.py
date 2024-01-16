"""Cmdb/waf/main-class connector."""

from fortigate_api.connector import Connector


class MainClassWC(Connector):
    """Cmdb/waf/main-class connector."""

    uid = "id"
    _path = "api/v2/cmdb/waf/main-class"
