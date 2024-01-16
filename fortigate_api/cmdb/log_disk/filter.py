"""Cmdb/log.disk/filter connector."""

from fortigate_api.connector import Connector


class FilterLdC(Connector):
    """Cmdb/log.disk/filter connector."""

    uid = ""
    _path = "api/v2/cmdb/log.disk/filter"
