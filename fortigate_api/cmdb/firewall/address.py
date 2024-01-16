"""Cmdb/firewall/address connector."""

from fortigate_api.connector import Connector


class AddressFC(Connector):
    """Cmdb/firewall/address connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/address"
    _path_ui = "ng/firewall/address"
