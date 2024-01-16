"""Cmdb/wireless-controller/access-control-list connector."""

from fortigate_api.connector import Connector


class AccessControlListWcC(Connector):
    """Cmdb/wireless-controller/access-control-list connector."""

    uid = "name"
    _path = "api/v2/cmdb/wireless-controller/access-control-list"
