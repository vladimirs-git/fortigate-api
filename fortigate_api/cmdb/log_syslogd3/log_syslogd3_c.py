"""Cmdb/log.syslogd3 connectors."""

from fortigate_api.cmdb.log_syslogd3.filter import FilterLsC
from fortigate_api.cmdb.log_syslogd3.override_filter import OverrideFilterLsC
from fortigate_api.cmdb.log_syslogd3.override_setting import OverrideSettingLsC
from fortigate_api.cmdb.log_syslogd3.setting import SettingLsC
from fortigate_api.fortigate import FortiGate


class LogSyslogd3C:
    """Cmdb/log.syslogd3 connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init LogSyslogd3C."""

        self.filter = FilterLsC(fortigate, **kwargs)
        """:py:class:`.FilterLsC` cmdb/log.syslogd3/filter."""

        self.override_filter = OverrideFilterLsC(fortigate, **kwargs)
        """:py:class:`.OverrideFilterLsC` cmdb/log.syslogd3/override-filter."""

        self.override_setting = OverrideSettingLsC(fortigate, **kwargs)
        """:py:class:`.OverrideSettingLsC` cmdb/log.syslogd3/override-setting."""

        self.setting = SettingLsC(fortigate, **kwargs)
        """:py:class:`.SettingLsC` cmdb/log.syslogd3/setting."""
