"""Cmdb/firewall/profile-group connector."""

from fortigate_api.connector import Connector


class ProfileGroupFC(Connector):
    """Cmdb/firewall/profile-group connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/profile-group"
