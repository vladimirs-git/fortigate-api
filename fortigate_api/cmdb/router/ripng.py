"""Cmdb/router/ripng connector."""

from fortigate_api.connector import Connector


class RipngRC(Connector):
    """Cmdb/router/ripng connector."""

    uid = ""
    _path = "api/v2/cmdb/router/ripng"
