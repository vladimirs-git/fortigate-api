"""Cmdb/log.fortianalyzer connectors."""

from fortigate_api.cmdb.log_fortianalyzer.filter import FilterLfC
from fortigate_api.cmdb.log_fortianalyzer.override_filter import OverrideFilterLfC
from fortigate_api.cmdb.log_fortianalyzer.override_setting import OverrideSettingLfC
from fortigate_api.cmdb.log_fortianalyzer.setting import SettingLfC
from fortigate_api.fortigate import FortiGate


class LogFortianalyzerC:
    """Cmdb/log.fortianalyzer connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init LogFortianalyzerC."""
        self.filter = FilterLfC(fortigate, **kwargs)
        """:py:class:`.FilterLfC` cmdb/log.fortianalyzer/filter."""

        self.override_filter = OverrideFilterLfC(fortigate, **kwargs)
        """:py:class:`.OverrideFilterLfC` cmdb/log.fortianalyzer/override-filter."""

        self.override_setting = OverrideSettingLfC(fortigate, **kwargs)
        """:py:class:`.OverrideSettingLfC` cmdb/log.fortianalyzer/override-setting."""

        self.setting = SettingLfC(fortigate, **kwargs)
        """:py:class:`.SettingLfC` cmdb/log.fortianalyzer/setting."""
