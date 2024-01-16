"""Cmdb/icap/profile connector."""

from fortigate_api.connector import Connector


class ProfileIC(Connector):
    """Cmdb/icap/profile connector."""

    uid = "name"
    _path = "api/v2/cmdb/icap/profile"
