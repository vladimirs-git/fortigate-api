"""Cmdb/log.syslogd/setting connector."""

from fortigate_api.connector import Connector


class SettingLsC(Connector):
    """Cmdb/log.syslogd/setting connector."""

    uid = ""
    _path = "api/v2/cmdb/log.syslogd/setting"
