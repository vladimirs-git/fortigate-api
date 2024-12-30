"""Cmdb/firewall.ssh connectors."""

from fortigate_api.cmdb.firewall_ssh.host_key import HostKeyFsC
from fortigate_api.cmdb.firewall_ssh.local_ca import LocalCaFsC
from fortigate_api.cmdb.firewall_ssh.local_key import LocalKeyFsC
from fortigate_api.cmdb.firewall_ssh.setting import SettingFsC
from fortigate_api.fortigate import FortiGate


class FirewallSshC:
    """Cmdb/firewall.ssh connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init FirewallSshC."""
        self.host_key = HostKeyFsC(fortigate, **kwargs)
        """:py:class:`.HostKeyFsC` cmdb/firewall.ssh/host-key."""

        self.local_ca = LocalCaFsC(fortigate, **kwargs)
        """:py:class:`.LocalCaFsC` cmdb/firewall.ssh/local-ca."""

        self.local_key = LocalKeyFsC(fortigate, **kwargs)
        """:py:class:`.LocalKeyFsC` cmdb/firewall.ssh/local-key."""

        self.setting = SettingFsC(fortigate, **kwargs)
        """:py:class:`.SettingFsC` cmdb/firewall.ssh/setting."""
