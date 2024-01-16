"""Cmdb/log.syslogd/override-setting connector."""

from fortigate_api.connector import Connector


class OverrideSettingLsC(Connector):
    """Cmdb/log.syslogd/override-setting connector."""

    uid = ""
    _path = "api/v2/cmdb/log.syslogd/override-setting"
