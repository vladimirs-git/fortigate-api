"""Cmdb/log.webtrends connectors."""

from fortigate_api.cmdb.log_webtrends.filter import FilterLwC
from fortigate_api.cmdb.log_webtrends.setting import SettingLwC
from fortigate_api.fortigate import FortiGate


class LogWebtrendsC:
    """Cmdb/log.webtrends connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init LogWebtrendsC."""
        self.filter = FilterLwC(fortigate, **kwargs)
        """:py:class:`.FilterLwC` cmdb/log.webtrends/filter."""

        self.setting = SettingLwC(fortigate, **kwargs)
        """:py:class:`.SettingLwC` cmdb/log.webtrends/setting."""
