"""Cmdb/log.syslogd2 connectors."""

from fortigate_api.cmdb.log_syslogd2.filter import FilterLsC
from fortigate_api.cmdb.log_syslogd2.override_filter import OverrideFilterLsC
from fortigate_api.cmdb.log_syslogd2.override_setting import OverrideSettingLsC
from fortigate_api.cmdb.log_syslogd2.setting import SettingLsC
from fortigate_api.fortigate import FortiGate


class LogSyslogd2C:
    """Cmdb/log.syslogd2 connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init LogSyslogd2C."""

        self.filter = FilterLsC(fortigate, **kwargs)
        """:py:class:`.FilterLsC` cmdb/log.syslogd2/filter."""

        self.override_filter = OverrideFilterLsC(fortigate, **kwargs)
        """:py:class:`.OverrideFilterLsC` cmdb/log.syslogd2/override-filter."""

        self.override_setting = OverrideSettingLsC(fortigate, **kwargs)
        """:py:class:`.OverrideSettingLsC` cmdb/log.syslogd2/override-setting."""

        self.setting = SettingLsC(fortigate, **kwargs)
        """:py:class:`.SettingLsC` cmdb/log.syslogd2/setting."""
