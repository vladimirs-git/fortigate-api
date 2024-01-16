"""Cmdb/log.syslogd/filter connector."""

from fortigate_api.connector import Connector


class FilterLsC(Connector):
    """Cmdb/log.syslogd/filter connector."""

    uid = ""
    _path = "api/v2/cmdb/log.syslogd/filter"
