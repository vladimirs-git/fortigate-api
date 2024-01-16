"""Cmdb/log.fortiguard/override-filter connector."""

from fortigate_api.connector import Connector


class OverrideFilterLfC(Connector):
    """Cmdb/log.fortiguard/override-filter connector."""

    uid = ""
    _path = "api/v2/cmdb/log.fortiguard/override-filter"
