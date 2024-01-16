"""Cmdb/firewall/internet-service-ipbl-vendor connector."""

from fortigate_api.connector import Connector


class InternetServiceIpblVendorFC(Connector):
    """Cmdb/firewall/internet-service-ipbl-vendor connector."""

    uid = "id"
    _path = "api/v2/cmdb/firewall/internet-service-ipbl-vendor"
