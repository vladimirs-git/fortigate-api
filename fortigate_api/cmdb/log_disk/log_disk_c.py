"""Cmdb/log.disk connectors."""

from fortigate_api.cmdb.log_disk.filter import FilterLdC
from fortigate_api.cmdb.log_disk.setting import SettingLdC
from fortigate_api.fortigate import FortiGate


class LogDiskC:
    """Cmdb/log.disk connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init LogDiskC."""
        self.filter = FilterLdC(fortigate, **kwargs)
        """:py:class:`.FilterLdC` cmdb/log.disk/filter."""

        self.setting = SettingLdC(fortigate, **kwargs)
        """:py:class:`.SettingLdC` cmdb/log.disk/setting."""
