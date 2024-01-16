"""Cmdb/user/pop3 connector."""

from fortigate_api.connector import Connector


class Pop3UC(Connector):
    """Cmdb/user/pop3 connector."""

    uid = "name"
    _path = "api/v2/cmdb/user/pop3"
