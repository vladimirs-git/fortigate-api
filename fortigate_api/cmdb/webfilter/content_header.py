"""Cmdb/webfilter/content-header connector."""

from fortigate_api.connector import Connector


class ContentHeaderWC(Connector):
    """Cmdb/webfilter/content-header connector."""

    uid = "id"
    _path = "api/v2/cmdb/webfilter/content-header"
