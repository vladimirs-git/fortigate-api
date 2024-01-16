"""Cmdb/ssh-filter/profile connector."""

from fortigate_api.connector import Connector


class ProfileSfC(Connector):
    """Cmdb/ssh-filter/profile connector."""

    uid = "name"
    _path = "api/v2/cmdb/ssh-filter/profile"
