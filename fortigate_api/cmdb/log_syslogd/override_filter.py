"""Cmdb/log.syslogd/override-filter connector."""

from fortigate_api.connector import Connector


class OverrideFilterLsC(Connector):
    """Cmdb/log.syslogd/override-filter connector."""

    uid = ""
    _path = "api/v2/cmdb/log.syslogd/override-filter"
