"""Cmdb/wireless-controller.hotspot20/qos-map connector."""

from fortigate_api.connector import Connector


class QosMapWchC(Connector):
    """Cmdb/wireless-controller.hotspot20/qos-map connector."""

    uid = "name"
    _path = "api/v2/cmdb/wireless-controller.hotspot20/qos-map"
