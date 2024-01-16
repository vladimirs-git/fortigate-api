"""Cmdb/wanopt/profile connector."""

from fortigate_api.connector import Connector


class ProfileWC(Connector):
    """Cmdb/wanopt/profile connector."""

    uid = "name"
    _path = "api/v2/cmdb/wanopt/profile"
