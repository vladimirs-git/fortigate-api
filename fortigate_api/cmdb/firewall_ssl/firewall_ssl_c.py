"""Cmdb/firewall.ssl connectors."""

from fortigate_api.cmdb.firewall_ssl.setting import SettingFsC
from fortigate_api.fortigate import FortiGate


class FirewallSslC:
    """Cmdb/firewall.ssl connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init FirewallSslC."""
        self.setting = SettingFsC(fortigate, **kwargs)
        """:py:class:`.SettingFsC` cmdb/firewall.ssl/setting."""
