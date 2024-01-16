"""Cmdb/web-proxy/explicit connector."""

from fortigate_api.connector import Connector


class ExplicitWpC(Connector):
    """Cmdb/web-proxy/explicit connector."""

    uid = ""
    _path = "api/v2/cmdb/web-proxy/explicit"
