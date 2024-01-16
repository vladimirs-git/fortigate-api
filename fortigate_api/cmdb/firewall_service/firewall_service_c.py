"""Cmdb/firewall.service connectors."""

from fortigate_api.cmdb.firewall_service.category import CategoryFsC
from fortigate_api.cmdb.firewall_service.custom import CustomFsC
from fortigate_api.cmdb.firewall_service.group import GroupFsC
from fortigate_api.fortigate import FortiGate


class FirewallServiceC:
    """Cmdb/firewall.service connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init FirewallServiceC."""

        self.category = CategoryFsC(fortigate, **kwargs)
        """:py:class:`.CategoryFsC` cmdb/firewall.service/category."""

        self.custom = CustomFsC(fortigate, **kwargs)
        """:py:class:`.CustomFsC` cmdb/firewall.service/custom."""

        self.group = GroupFsC(fortigate, **kwargs)
        """:py:class:`.GroupFsC` cmdb/firewall.service/group."""
