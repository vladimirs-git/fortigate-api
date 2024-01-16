"""Cmdb/router/prefix-list connector."""

from fortigate_api.connector import Connector


class PrefixListRC(Connector):
    """Cmdb/router/prefix-list connector."""

    uid = "name"
    _path = "api/v2/cmdb/router/prefix-list"
