"""Cmdb/webfilter/content connector."""

from fortigate_api.connector import Connector


class ContentWC(Connector):
    """Cmdb/webfilter/content connector."""

    uid = "id"
    _path = "api/v2/cmdb/webfilter/content"
