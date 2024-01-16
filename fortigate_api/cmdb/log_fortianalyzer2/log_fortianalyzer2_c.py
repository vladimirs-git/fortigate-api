"""Cmdb/log.fortianalyzer2 connectors."""

from fortigate_api.cmdb.log_fortianalyzer2.filter import FilterLfC
from fortigate_api.cmdb.log_fortianalyzer2.override_filter import OverrideFilterLfC
from fortigate_api.cmdb.log_fortianalyzer2.override_setting import OverrideSettingLfC
from fortigate_api.cmdb.log_fortianalyzer2.setting import SettingLfC
from fortigate_api.fortigate import FortiGate


class LogFortianalyzer2C:
    """Cmdb/log.fortianalyzer2 connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init LogFortianalyzer2C."""

        self.filter = FilterLfC(fortigate, **kwargs)
        """:py:class:`.FilterLfC` cmdb/log.fortianalyzer2/filter."""

        self.override_filter = OverrideFilterLfC(fortigate, **kwargs)
        """:py:class:`.OverrideFilterLfC` cmdb/log.fortianalyzer2/override-filter."""

        self.override_setting = OverrideSettingLfC(fortigate, **kwargs)
        """:py:class:`.OverrideSettingLfC` cmdb/log.fortianalyzer2/override-setting."""

        self.setting = SettingLfC(fortigate, **kwargs)
        """:py:class:`.SettingLfC` cmdb/log.fortianalyzer2/setting."""
