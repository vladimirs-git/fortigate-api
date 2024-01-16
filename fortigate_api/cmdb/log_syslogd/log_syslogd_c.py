"""Cmdb/log.syslogd connectors."""

from fortigate_api.cmdb.log_syslogd.filter import FilterLsC
from fortigate_api.cmdb.log_syslogd.override_filter import OverrideFilterLsC
from fortigate_api.cmdb.log_syslogd.override_setting import OverrideSettingLsC
from fortigate_api.cmdb.log_syslogd.setting import SettingLsC
from fortigate_api.fortigate import FortiGate


class LogSyslogdC:
    """Cmdb/log.syslogd connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init LogSyslogdC."""

        self.filter = FilterLsC(fortigate, **kwargs)
        """:py:class:`.FilterLsC` cmdb/log.syslogd/filter."""

        self.override_filter = OverrideFilterLsC(fortigate, **kwargs)
        """:py:class:`.OverrideFilterLsC` cmdb/log.syslogd/override-filter."""

        self.override_setting = OverrideSettingLsC(fortigate, **kwargs)
        """:py:class:`.OverrideSettingLsC` cmdb/log.syslogd/override-setting."""

        self.setting = SettingLsC(fortigate, **kwargs)
        """:py:class:`.SettingLsC` cmdb/log.syslogd/setting."""
