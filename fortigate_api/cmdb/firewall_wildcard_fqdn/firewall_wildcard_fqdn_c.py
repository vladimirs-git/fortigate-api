"""Cmdb/firewall.wildcard-fqdn connectors."""

from fortigate_api.cmdb.firewall_wildcard_fqdn.custom import CustomFwfC
from fortigate_api.cmdb.firewall_wildcard_fqdn.group import GroupFwfC
from fortigate_api.fortigate import FortiGate


class FirewallWildcardFqdnC:
    """Cmdb/firewall.wildcard-fqdn connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init FirewallWildcardFqdnC."""

        self.custom = CustomFwfC(fortigate, **kwargs)
        """:py:class:`.CustomFwfC` cmdb/firewall.wildcard-fqdn/custom."""

        self.group = GroupFwfC(fortigate, **kwargs)
        """:py:class:`.GroupFwfC` cmdb/firewall.wildcard-fqdn/group."""
