"""Cmdb/web-proxy/url-match connector."""

from fortigate_api.connector import Connector


class UrlMatchWpC(Connector):
    """Cmdb/web-proxy/url-match connector."""

    uid = "name"
    _path = "api/v2/cmdb/web-proxy/url-match"
