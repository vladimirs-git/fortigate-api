"""Cmdb/system/geneve connector."""

from fortigate_api.connector import Connector


class GeneveSC(Connector):
    """Cmdb/system/geneve connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/geneve"
