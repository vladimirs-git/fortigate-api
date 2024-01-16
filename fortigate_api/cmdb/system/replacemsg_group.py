"""Cmdb/system/replacemsg-group connector."""

from fortigate_api.connector import Connector


class ReplacemsgGroupSC(Connector):
    """Cmdb/system/replacemsg-group connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/replacemsg-group"
