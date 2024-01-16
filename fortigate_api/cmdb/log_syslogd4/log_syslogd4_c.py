"""Cmdb/log.syslogd4 connectors."""

from fortigate_api.cmdb.log_syslogd4.filter import FilterLsC
from fortigate_api.cmdb.log_syslogd4.override_filter import OverrideFilterLsC
from fortigate_api.cmdb.log_syslogd4.override_setting import OverrideSettingLsC
from fortigate_api.cmdb.log_syslogd4.setting import SettingLsC
from fortigate_api.fortigate import FortiGate


class LogSyslogd4C:
    """Cmdb/log.syslogd4 connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init LogSyslogd4C."""

        self.filter = FilterLsC(fortigate, **kwargs)
        """:py:class:`.FilterLsC` cmdb/log.syslogd4/filter."""

        self.override_filter = OverrideFilterLsC(fortigate, **kwargs)
        """:py:class:`.OverrideFilterLsC` cmdb/log.syslogd4/override-filter."""

        self.override_setting = OverrideSettingLsC(fortigate, **kwargs)
        """:py:class:`.OverrideSettingLsC` cmdb/log.syslogd4/override-setting."""

        self.setting = SettingLsC(fortigate, **kwargs)
        """:py:class:`.SettingLsC` cmdb/log.syslogd4/setting."""
