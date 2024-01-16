"""Cmdb/emailfilter/profile connector."""

from fortigate_api.connector import Connector


class ProfileEC(Connector):
    """Cmdb/emailfilter/profile connector."""

    uid = "name"
    _path = "api/v2/cmdb/emailfilter/profile"
