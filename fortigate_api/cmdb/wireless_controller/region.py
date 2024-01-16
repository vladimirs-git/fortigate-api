"""Cmdb/wireless-controller/region connector."""

from fortigate_api.connector import Connector


class RegionWcC(Connector):
    """Cmdb/wireless-controller/region connector."""

    uid = "name"
    _path = "api/v2/cmdb/wireless-controller/region"
