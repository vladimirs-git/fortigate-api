"""Cmdb/wireless-controller/vap-group connector."""

from fortigate_api.connector import Connector


class VapGroupWcC(Connector):
    """Cmdb/wireless-controller/vap-group connector."""

    uid = "name"
    _path = "api/v2/cmdb/wireless-controller/vap-group"
