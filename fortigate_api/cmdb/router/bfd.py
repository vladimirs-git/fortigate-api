"""Cmdb/router/bfd connector."""

from fortigate_api.connector import Connector


class BfdRC(Connector):
    """Cmdb/router/bfd connector."""

    uid = ""
    _path = "api/v2/cmdb/router/bfd"
