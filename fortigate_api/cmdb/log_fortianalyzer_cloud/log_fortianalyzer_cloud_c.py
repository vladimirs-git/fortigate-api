"""Cmdb/log.fortianalyzer-cloud connectors."""

from fortigate_api.cmdb.log_fortianalyzer_cloud.filter import FilterLfcC
from fortigate_api.cmdb.log_fortianalyzer_cloud.override_filter import OverrideFilterLfcC
from fortigate_api.cmdb.log_fortianalyzer_cloud.override_setting import OverrideSettingLfcC
from fortigate_api.cmdb.log_fortianalyzer_cloud.setting import SettingLfcC
from fortigate_api.fortigate import FortiGate


class LogFortianalyzerCloudC:
    """Cmdb/log.fortianalyzer-cloud connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init LogFortianalyzerCloudC."""

        self.filter = FilterLfcC(fortigate, **kwargs)
        """:py:class:`.FilterLfcC` cmdb/log.fortianalyzer-cloud/filter."""

        self.override_filter = OverrideFilterLfcC(fortigate, **kwargs)
        """:py:class:`.OverrideFilterLfcC` cmdb/log.fortianalyzer-cloud/override-filter."""

        self.override_setting = OverrideSettingLfcC(fortigate, **kwargs)
        """:py:class:`.OverrideSettingLfcC` cmdb/log.fortianalyzer-cloud/override-setting."""

        self.setting = SettingLfcC(fortigate, **kwargs)
        """:py:class:`.SettingLfcC` cmdb/log.fortianalyzer-cloud/setting."""
