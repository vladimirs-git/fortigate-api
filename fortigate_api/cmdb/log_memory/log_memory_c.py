"""Cmdb/log.memory connectors."""

from fortigate_api.cmdb.log_memory.filter import FilterLmC
from fortigate_api.cmdb.log_memory.global_setting import GlobalSettingLmC
from fortigate_api.cmdb.log_memory.setting import SettingLmC
from fortigate_api.fortigate import FortiGate


class LogMemoryC:
    """Cmdb/log.memory connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init LogMemoryC."""

        self.filter = FilterLmC(fortigate, **kwargs)
        """:py:class:`.FilterLmC` cmdb/log.memory/filter."""

        self.global_setting = GlobalSettingLmC(fortigate, **kwargs)
        """:py:class:`.GlobalSettingLmC` cmdb/log.memory/global-setting."""

        self.setting = SettingLmC(fortigate, **kwargs)
        """:py:class:`.SettingLmC` cmdb/log.memory/setting."""
