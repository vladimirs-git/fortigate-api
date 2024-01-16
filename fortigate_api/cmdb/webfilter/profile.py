"""Cmdb/webfilter/profile connector."""

from fortigate_api.connector import Connector


class ProfileWC(Connector):
    """Cmdb/webfilter/profile connector."""

    uid = "name"
    _path = "api/v2/cmdb/webfilter/profile"
