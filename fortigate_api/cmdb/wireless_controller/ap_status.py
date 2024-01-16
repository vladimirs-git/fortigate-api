"""Cmdb/wireless-controller/ap-status connector."""

from fortigate_api.connector import Connector


class ApStatusWcC(Connector):
    """Cmdb/wireless-controller/ap-status connector."""

    uid = "id"
    _path = "api/v2/cmdb/wireless-controller/ap-status"
