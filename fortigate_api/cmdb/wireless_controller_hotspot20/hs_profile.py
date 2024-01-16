"""Cmdb/wireless-controller.hotspot20/hs-profile connector."""

from fortigate_api.connector import Connector


class HsProfileWchC(Connector):
    """Cmdb/wireless-controller.hotspot20/hs-profile connector."""

    uid = "name"
    _path = "api/v2/cmdb/wireless-controller.hotspot20/hs-profile"
