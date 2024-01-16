"""Cmdb/application/list connector."""

from fortigate_api.connector import Connector


class ListAC(Connector):
    """Cmdb/application/list connector."""

    uid = "name"
    _path = "api/v2/cmdb/application/list"
    _path_ui = "ng/utm/appctrl/sensor"
