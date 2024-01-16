"""Cmdb/extender-controller/dataplan connector."""

from fortigate_api.connector import Connector


class DataplanEcC(Connector):
    """Cmdb/extender-controller/dataplan connector."""

    uid = "name"
    _path = "api/v2/cmdb/extender-controller/dataplan"
