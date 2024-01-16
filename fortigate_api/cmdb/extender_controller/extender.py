"""Cmdb/extender-controller/extender connector."""

from fortigate_api.connector import Connector


class ExtenderEcC(Connector):
    """Cmdb/extender-controller/extender connector."""

    uid = "name"
    _path = "api/v2/cmdb/extender-controller/extender"
