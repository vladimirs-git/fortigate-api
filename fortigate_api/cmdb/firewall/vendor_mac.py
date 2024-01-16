"""Cmdb/firewall/vendor-mac connector."""

from fortigate_api.connector import Connector


class VendorMacFC(Connector):
    """Cmdb/firewall/vendor-mac connector."""

    uid = "id"
    _path = "api/v2/cmdb/firewall/vendor-mac"
