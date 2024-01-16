"""Cmdb/router/policy6 connector."""

from fortigate_api.connector import Connector


class Policy6RC(Connector):
    """Cmdb/router/policy6 connector."""

    uid = "seq-num"
    _path = "api/v2/cmdb/router/policy6"
