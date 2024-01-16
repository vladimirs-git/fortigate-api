"""Cmdb/switch-controller.initial-config connectors."""

from fortigate_api.cmdb.switch_controller_initial_config.template import TemplateScicC
from fortigate_api.cmdb.switch_controller_initial_config.vlans import VlansScicC
from fortigate_api.fortigate import FortiGate


class SwitchControllerInitialConfigC:
    """Cmdb/switch-controller.initial-config connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init SwitchControllerInitialConfigC."""

        self.template = TemplateScicC(fortigate, **kwargs)
        """:py:class:`.TemplateScicC` cmdb/switch-controller.initial-config/template."""

        self.vlans = VlansScicC(fortigate, **kwargs)
        """:py:class:`.VlansScicC` cmdb/switch-controller.initial-config/vlans."""
