"""Cmdb/router/prefix-list6 connector."""

from fortigate_api.connector import Connector


class PrefixList6RC(Connector):
    """Cmdb/router/prefix-list6 connector."""

    uid = "name"
    _path = "api/v2/cmdb/router/prefix-list6"
