"""Cmdb/firewall.ipmacbinding connectors."""

from fortigate_api.cmdb.firewall_ipmacbinding.setting import SettingFiC
from fortigate_api.cmdb.firewall_ipmacbinding.table import TableFiC
from fortigate_api.fortigate import FortiGate


class FirewallIpmacbindingC:
    """Cmdb/firewall.ipmacbinding connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init FirewallIpmacbindingC."""
        self.setting = SettingFiC(fortigate, **kwargs)
        """:py:class:`.SettingFiC` cmdb/firewall.ipmacbinding/setting."""

        self.table = TableFiC(fortigate, **kwargs)
        """:py:class:`.TableFiC` cmdb/firewall.ipmacbinding/table."""
