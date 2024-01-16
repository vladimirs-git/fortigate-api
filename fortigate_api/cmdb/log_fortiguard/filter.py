"""Cmdb/log.fortiguard/filter connector."""

from fortigate_api.connector import Connector


class FilterLfC(Connector):
    """Cmdb/log.fortiguard/filter connector."""

    uid = ""
    _path = "api/v2/cmdb/log.fortiguard/filter"
