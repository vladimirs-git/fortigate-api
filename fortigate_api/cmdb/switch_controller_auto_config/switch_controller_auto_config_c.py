"""Cmdb/switch-controller.auto-config connectors."""

from fortigate_api.cmdb.switch_controller_auto_config.default import DefaultScacC
from fortigate_api.fortigate import FortiGate


class SwitchControllerAutoConfigC:
    """Cmdb/switch-controller.auto-config connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init SwitchControllerAutoConfigC."""

        self.default = DefaultScacC(fortigate, **kwargs)
        """:py:class:`.DefaultScacC` cmdb/switch-controller.auto-config/default."""
