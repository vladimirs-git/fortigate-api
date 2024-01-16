"""Cmdb/emailfilter/bwl connector."""

from fortigate_api.connector import Connector


class BwlEC(Connector):
    """Cmdb/emailfilter/bwl connector."""

    uid = "id"
    _path = "api/v2/cmdb/emailfilter/bwl"
