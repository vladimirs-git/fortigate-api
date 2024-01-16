"""Cmdb/system/wccp connector."""

from fortigate_api.connector import Connector


class WccpSC(Connector):
    """Cmdb/system/wccp connector."""

    uid = "service-id"
    _path = "api/v2/cmdb/system/wccp"
