"""Cmdb/log.null-device connectors."""

from fortigate_api.cmdb.log_null_device.filter import FilterLndC
from fortigate_api.cmdb.log_null_device.setting import SettingLndC
from fortigate_api.fortigate import FortiGate


class LogNullDeviceC:
    """Cmdb/log.null-device connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init LogNullDeviceC."""

        self.filter = FilterLndC(fortigate, **kwargs)
        """:py:class:`.FilterLndC` cmdb/log.null-device/filter."""

        self.setting = SettingLndC(fortigate, **kwargs)
        """:py:class:`.SettingLndC` cmdb/log.null-device/setting."""
