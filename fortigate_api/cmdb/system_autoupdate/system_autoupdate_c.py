"""Cmdb/system.autoupdate connectors."""

from fortigate_api.cmdb.system_autoupdate.push_update import PushUpdateSaC
from fortigate_api.cmdb.system_autoupdate.schedule import ScheduleSaC
from fortigate_api.cmdb.system_autoupdate.tunneling import TunnelingSaC
from fortigate_api.fortigate import FortiGate


class SystemAutoupdateC:
    """Cmdb/system.autoupdate connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init SystemAutoupdateC."""

        self.push_update = PushUpdateSaC(fortigate, **kwargs)
        """:py:class:`.PushUpdateSaC` cmdb/system.autoupdate/push-update."""

        self.schedule = ScheduleSaC(fortigate, **kwargs)
        """:py:class:`.ScheduleSaC` cmdb/system.autoupdate/schedule."""

        self.tunneling = TunnelingSaC(fortigate, **kwargs)
        """:py:class:`.TunnelingSaC` cmdb/system.autoupdate/tunneling."""
