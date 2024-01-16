"""Cmdb/file-filter/profile connector."""

from fortigate_api.connector import Connector


class ProfileFfC(Connector):
    """Cmdb/file-filter/profile connector."""

    uid = "name"
    _path = "api/v2/cmdb/file-filter/profile"
