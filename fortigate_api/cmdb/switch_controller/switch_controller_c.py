"""Cmdb/switch-controller connectors."""

from fortigate_api.cmdb.switch_controller.global_ import GlobalScC
from fortigate_api.cmdb.switch_controller.lldp_profile import LldpProfileScC
from fortigate_api.cmdb.switch_controller.lldp_settings import LldpSettingsScC
from fortigate_api.cmdb.switch_controller.location import LocationScC
from fortigate_api.cmdb.switch_controller.mac_policy import MacPolicyScC
from fortigate_api.cmdb.switch_controller.managed_switch import ManagedSwitchScC
from fortigate_api.cmdb.switch_controller.nac_device import NacDeviceScC
from fortigate_api.cmdb.switch_controller.nac_settings import NacSettingsScC
from fortigate_api.cmdb.switch_controller.port_policy import PortPolicyScC
from fortigate_api.cmdb.switch_controller.snmp_community import SnmpCommunityScC
from fortigate_api.cmdb.switch_controller.stp_instance import StpInstanceScC
from fortigate_api.cmdb.switch_controller.stp_settings import StpSettingsScC
from fortigate_api.cmdb.switch_controller.switch_group import SwitchGroupScC
from fortigate_api.cmdb.switch_controller.system import SystemScC
from fortigate_api.cmdb.switch_controller.vlan_policy import VlanPolicyScC
from fortigate_api.fortigate import FortiGate


class SwitchControllerC:
    """Cmdb/switch-controller connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init SwitchControllerC."""

        self.global_ = GlobalScC(fortigate, **kwargs)
        """:py:class:`.GlobalScC` cmdb/switch-controller/global."""

        self.lldp_profile = LldpProfileScC(fortigate, **kwargs)
        """:py:class:`.LldpProfileScC` cmdb/switch-controller/lldp-profile."""

        self.lldp_settings = LldpSettingsScC(fortigate, **kwargs)
        """:py:class:`.LldpSettingsScC` cmdb/switch-controller/lldp-settings."""

        self.location = LocationScC(fortigate, **kwargs)
        """:py:class:`.LocationScC` cmdb/switch-controller/location."""

        self.mac_policy = MacPolicyScC(fortigate, **kwargs)
        """:py:class:`.MacPolicyScC` cmdb/switch-controller/mac-policy."""

        self.managed_switch = ManagedSwitchScC(fortigate, **kwargs)
        """:py:class:`.ManagedSwitchScC` cmdb/switch-controller/managed-switch."""

        self.nac_device = NacDeviceScC(fortigate, **kwargs)
        """:py:class:`.NacDeviceScC` cmdb/switch-controller/nac-device."""

        self.nac_settings = NacSettingsScC(fortigate, **kwargs)
        """:py:class:`.NacSettingsScC` cmdb/switch-controller/nac-settings."""

        self.port_policy = PortPolicyScC(fortigate, **kwargs)
        """:py:class:`.PortPolicyScC` cmdb/switch-controller/port-policy."""

        self.snmp_community = SnmpCommunityScC(fortigate, **kwargs)
        """:py:class:`.SnmpCommunityScC` cmdb/switch-controller/snmp-community."""

        self.stp_instance = StpInstanceScC(fortigate, **kwargs)
        """:py:class:`.StpInstanceScC` cmdb/switch-controller/stp-instance."""

        self.stp_settings = StpSettingsScC(fortigate, **kwargs)
        """:py:class:`.StpSettingsScC` cmdb/switch-controller/stp-settings."""

        self.switch_group = SwitchGroupScC(fortigate, **kwargs)
        """:py:class:`.SwitchGroupScC` cmdb/switch-controller/switch-group."""

        self.system = SystemScC(fortigate, **kwargs)
        """:py:class:`.SystemScC` cmdb/switch-controller/system."""

        self.vlan_policy = VlanPolicyScC(fortigate, **kwargs)
        """:py:class:`.VlanPolicyScC` cmdb/switch-controller/vlan-policy."""
