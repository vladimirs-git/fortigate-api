"""Cmdb/system/ddns connector."""

from fortigate_api.connector import Connector


class DdnsSC(Connector):
    """Cmdb/system/ddns connector."""

    uid = "ddnsid"
    _path = "api/v2/cmdb/system/ddns"
