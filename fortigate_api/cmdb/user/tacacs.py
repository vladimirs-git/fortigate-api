"""Cmdb/user/tacacs+ connector."""

from fortigate_api.connector import Connector


class TacacsUC(Connector):
    """Cmdb/user/tacacs+ connector."""

    uid = "name"
    _path = "api/v2/cmdb/user/tacacs+"
