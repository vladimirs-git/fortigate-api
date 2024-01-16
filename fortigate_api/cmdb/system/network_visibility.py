"""Cmdb/system/network-visibility connector."""

from fortigate_api.connector import Connector


class NetworkVisibilitySC(Connector):
    """Cmdb/system/network-visibility connector."""

    uid = ""
    _path = "api/v2/cmdb/system/network-visibility"
