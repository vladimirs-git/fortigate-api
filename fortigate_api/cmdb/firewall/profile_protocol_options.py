"""Cmdb/firewall/profile-protocol-options connector."""

from fortigate_api.connector import Connector


class ProfileProtocolOptionsFC(Connector):
    """Cmdb/firewall/profile-protocol-options connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/profile-protocol-options"
