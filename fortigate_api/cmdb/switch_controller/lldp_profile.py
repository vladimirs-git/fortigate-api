"""Cmdb/switch-controller/lldp-profile connector."""

from fortigate_api.connector import Connector


class LldpProfileScC(Connector):
    """Cmdb/switch-controller/lldp-profile connector."""

    uid = "name"
    _path = "api/v2/cmdb/switch-controller/lldp-profile"
