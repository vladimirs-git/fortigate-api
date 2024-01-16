"""Cmdb/system.lldp connectors."""

from fortigate_api.cmdb.system_lldp.network_policy import NetworkPolicySlC
from fortigate_api.fortigate import FortiGate


class SystemLldpC:
    """Cmdb/system.lldp connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init SystemLldpC."""

        self.network_policy = NetworkPolicySlC(fortigate, **kwargs)
        """:py:class:`.NetworkPolicySlC` cmdb/system.lldp/network-policy."""
