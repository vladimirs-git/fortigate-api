"""Cmdb/report connectors."""

from fortigate_api.cmdb.report.chart import ChartRC
from fortigate_api.cmdb.report.dataset import DatasetRC
from fortigate_api.cmdb.report.layout import LayoutRC
from fortigate_api.cmdb.report.setting import SettingRC
from fortigate_api.cmdb.report.style import StyleRC
from fortigate_api.cmdb.report.theme import ThemeRC
from fortigate_api.fortigate import FortiGate


class ReportC:
    """Cmdb/report connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init ReportC."""
        self.chart = ChartRC(fortigate, **kwargs)
        """:py:class:`.ChartRC` cmdb/report/chart."""

        self.dataset = DatasetRC(fortigate, **kwargs)
        """:py:class:`.DatasetRC` cmdb/report/dataset."""

        self.layout = LayoutRC(fortigate, **kwargs)
        """:py:class:`.LayoutRC` cmdb/report/layout."""

        self.setting = SettingRC(fortigate, **kwargs)
        """:py:class:`.SettingRC` cmdb/report/setting."""

        self.style = StyleRC(fortigate, **kwargs)
        """:py:class:`.StyleRC` cmdb/report/style."""

        self.theme = ThemeRC(fortigate, **kwargs)
        """:py:class:`.ThemeRC` cmdb/report/theme."""
