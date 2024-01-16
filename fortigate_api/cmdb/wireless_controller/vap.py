"""Cmdb/wireless-controller/vap connector."""

from fortigate_api.connector import Connector


class VapWcC(Connector):
    """Cmdb/wireless-controller/vap connector."""

    uid = "name"
    _path = "api/v2/cmdb/wireless-controller/vap"
