"""Cmdb/router/rip connector."""

from fortigate_api.connector import Connector


class RipRC(Connector):
    """Cmdb/router/rip connector."""

    uid = ""
    _path = "api/v2/cmdb/router/rip"
