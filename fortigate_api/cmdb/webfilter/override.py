"""Cmdb/webfilter/override connector."""

from fortigate_api.connector import Connector


class OverrideWC(Connector):
    """Cmdb/webfilter/override connector."""

    uid = "id"
    _path = "api/v2/cmdb/webfilter/override"
