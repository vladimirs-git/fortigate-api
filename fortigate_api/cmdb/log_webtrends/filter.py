"""Cmdb/log.webtrends/filter connector."""

from fortigate_api.connector import Connector


class FilterLwC(Connector):
    """Cmdb/log.webtrends/filter connector."""

    uid = ""
    _path = "api/v2/cmdb/log.webtrends/filter"
