"""Cmdb/waf/profile connector."""

from fortigate_api.connector import Connector


class ProfileWC(Connector):
    """Cmdb/waf/profile connector."""

    uid = "name"
    _path = "api/v2/cmdb/waf/profile"
