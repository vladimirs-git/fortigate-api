"""Cmdb/log.fortiguard connectors."""

from fortigate_api.cmdb.log_fortiguard.filter import FilterLfC
from fortigate_api.cmdb.log_fortiguard.override_filter import OverrideFilterLfC
from fortigate_api.cmdb.log_fortiguard.override_setting import OverrideSettingLfC
from fortigate_api.cmdb.log_fortiguard.setting import SettingLfC
from fortigate_api.fortigate import FortiGate


class LogFortiguardC:
    """Cmdb/log.fortiguard connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init LogFortiguardC."""
        self.filter = FilterLfC(fortigate, **kwargs)
        """:py:class:`.FilterLfC` cmdb/log.fortiguard/filter."""

        self.override_filter = OverrideFilterLfC(fortigate, **kwargs)
        """:py:class:`.OverrideFilterLfC` cmdb/log.fortiguard/override-filter."""

        self.override_setting = OverrideSettingLfC(fortigate, **kwargs)
        """:py:class:`.OverrideSettingLfC` cmdb/log.fortiguard/override-setting."""

        self.setting = SettingLfC(fortigate, **kwargs)
        """:py:class:`.SettingLfC` cmdb/log.fortiguard/setting."""
