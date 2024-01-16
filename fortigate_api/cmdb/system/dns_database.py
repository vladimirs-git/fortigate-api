"""Cmdb/system/dns-database connector."""

from fortigate_api.connector import Connector


class DnsDatabaseSC(Connector):
    """Cmdb/system/dns-database connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/dns-database"
