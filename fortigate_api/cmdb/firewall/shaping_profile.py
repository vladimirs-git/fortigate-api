"""Cmdb/firewall/shaping-profile connector."""

from fortigate_api.connector import Connector


class ShapingProfileFC(Connector):
    """Cmdb/firewall/shaping-profile connector."""

    uid = "profile-name"
    _path = "api/v2/cmdb/firewall/shaping-profile"
