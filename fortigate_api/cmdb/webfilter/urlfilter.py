"""Cmdb/webfilter/urlfilter connector."""

from fortigate_api.connector import Connector


class UrlfilterWC(Connector):
    """Cmdb/webfilter/urlfilter connector."""

    uid = "id"
    _path = "api/v2/cmdb/webfilter/urlfilter"
