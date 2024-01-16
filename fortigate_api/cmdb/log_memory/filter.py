"""Cmdb/log.memory/filter connector."""

from fortigate_api.connector import Connector


class FilterLmC(Connector):
    """Cmdb/log.memory/filter connector."""

    uid = ""
    _path = "api/v2/cmdb/log.memory/filter"
