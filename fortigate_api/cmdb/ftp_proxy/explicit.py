"""Cmdb/ftp-proxy/explicit connector."""

from fortigate_api.connector import Connector


class ExplicitFpC(Connector):
    """Cmdb/ftp-proxy/explicit connector."""

    uid = ""
    _path = "api/v2/cmdb/ftp-proxy/explicit"
