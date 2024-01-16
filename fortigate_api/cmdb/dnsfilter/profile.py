"""Cmdb/dnsfilter/profile connector."""

from fortigate_api.connector import Connector


class ProfileDC(Connector):
    """Cmdb/dnsfilter/profile connector."""

    uid = "name"
    _path = "api/v2/cmdb/dnsfilter/profile"
