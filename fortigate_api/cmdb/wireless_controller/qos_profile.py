"""Cmdb/wireless-controller/qos-profile connector."""

from fortigate_api.connector import Connector


class QosProfileWcC(Connector):
    """Cmdb/wireless-controller/qos-profile connector."""

    uid = "name"
    _path = "api/v2/cmdb/wireless-controller/qos-profile"
