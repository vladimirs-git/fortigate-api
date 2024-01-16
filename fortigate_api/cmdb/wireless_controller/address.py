"""Cmdb/wireless-controller/address connector."""

from fortigate_api.connector import Connector


class AddressWcC(Connector):
    """Cmdb/wireless-controller/address connector."""

    uid = "id"
    _path = "api/v2/cmdb/wireless-controller/address"
