"""Cmdb/log.fortianalyzer3 connectors."""

from fortigate_api.cmdb.log_fortianalyzer3.filter import FilterLfC
from fortigate_api.cmdb.log_fortianalyzer3.override_filter import OverrideFilterLfC
from fortigate_api.cmdb.log_fortianalyzer3.override_setting import OverrideSettingLfC
from fortigate_api.cmdb.log_fortianalyzer3.setting import SettingLfC
from fortigate_api.fortigate import FortiGate


class LogFortianalyzer3C:
    """Cmdb/log.fortianalyzer3 connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init LogFortianalyzer3C."""
        self.filter = FilterLfC(fortigate, **kwargs)
        """:py:class:`.FilterLfC` cmdb/log.fortianalyzer3/filter."""

        self.override_filter = OverrideFilterLfC(fortigate, **kwargs)
        """:py:class:`.OverrideFilterLfC` cmdb/log.fortianalyzer3/override-filter."""

        self.override_setting = OverrideSettingLfC(fortigate, **kwargs)
        """:py:class:`.OverrideSettingLfC` cmdb/log.fortianalyzer3/override-setting."""

        self.setting = SettingLfC(fortigate, **kwargs)
        """:py:class:`.SettingLfC` cmdb/log.fortianalyzer3/setting."""
