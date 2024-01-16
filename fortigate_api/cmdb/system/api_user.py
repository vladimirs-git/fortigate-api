"""Cmdb/system/api-user connector."""

from fortigate_api.connector import Connector


class ApiUserSC(Connector):
    """Cmdb/system/api-user connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/api-user"
