"""Cmdb/voip/profile connector."""

from fortigate_api.connector import Connector


class ProfileVC(Connector):
    """Cmdb/voip/profile connector."""

    uid = "name"
    _path = "api/v2/cmdb/voip/profile"
