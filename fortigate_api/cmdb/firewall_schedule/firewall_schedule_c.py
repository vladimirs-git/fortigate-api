"""Cmdb/firewall.schedule connectors."""

from fortigate_api.cmdb.firewall_schedule.group import GroupFsC
from fortigate_api.cmdb.firewall_schedule.onetime import OnetimeFsC
from fortigate_api.cmdb.firewall_schedule.recurring import RecurringFsC
from fortigate_api.fortigate import FortiGate


class FirewallScheduleC:
    """Cmdb/firewall.schedule connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init FirewallScheduleC."""

        self.group = GroupFsC(fortigate, **kwargs)
        """:py:class:`.GroupFsC` cmdb/firewall.schedule/group."""

        self.onetime = OnetimeFsC(fortigate, **kwargs)
        """:py:class:`.OnetimeFsC` cmdb/firewall.schedule/onetime."""

        self.recurring = RecurringFsC(fortigate, **kwargs)
        """:py:class:`.RecurringFsC` cmdb/firewall.schedule/recurring."""
