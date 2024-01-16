"""Cmdb/system connectors."""

from fortigate_api.cmdb.system.accprofile import AccprofileSC
from fortigate_api.cmdb.system.admin import AdminSC
from fortigate_api.cmdb.system.alarm import AlarmSC
from fortigate_api.cmdb.system.api_user import ApiUserSC
from fortigate_api.cmdb.system.arp_table import ArpTableSC
from fortigate_api.cmdb.system.auto_install import AutoInstallSC
from fortigate_api.cmdb.system.auto_script import AutoScriptSC
from fortigate_api.cmdb.system.automation_action import AutomationActionSC
from fortigate_api.cmdb.system.automation_destination import AutomationDestinationSC
from fortigate_api.cmdb.system.automation_stitch import AutomationStitchSC
from fortigate_api.cmdb.system.automation_trigger import AutomationTriggerSC
from fortigate_api.cmdb.system.central_management import CentralManagementSC
from fortigate_api.cmdb.system.cluster_sync import ClusterSyncSC
from fortigate_api.cmdb.system.console import ConsoleSC
from fortigate_api.cmdb.system.csf import CsfSC
from fortigate_api.cmdb.system.custom_language import CustomLanguageSC
from fortigate_api.cmdb.system.ddns import DdnsSC
from fortigate_api.cmdb.system.dedicated_mgmt import DedicatedMgmtSC
from fortigate_api.cmdb.system.dns import DnsSC
from fortigate_api.cmdb.system.dns_database import DnsDatabaseSC
from fortigate_api.cmdb.system.dns_server import DnsServerSC
from fortigate_api.cmdb.system.dscp_based_priority import DscpBasedPrioritySC
from fortigate_api.cmdb.system.email_server import EmailServerSC
from fortigate_api.cmdb.system.external_resource import ExternalResourceSC
from fortigate_api.cmdb.system.fips_cc import FipsCcSC
from fortigate_api.cmdb.system.fortiguard import FortiguardSC
from fortigate_api.cmdb.system.fortimanager import FortimanagerSC
from fortigate_api.cmdb.system.fortisandbox import FortisandboxSC
from fortigate_api.cmdb.system.fsso_polling import FssoPollingSC
from fortigate_api.cmdb.system.ftm_push import FtmPushSC
from fortigate_api.cmdb.system.geneve import GeneveSC
from fortigate_api.cmdb.system.geoip_country import GeoipCountrySC
from fortigate_api.cmdb.system.geoip_override import GeoipOverrideSC
from fortigate_api.cmdb.system.global_ import GlobalSC
from fortigate_api.cmdb.system.gre_tunnel import GreTunnelSC
from fortigate_api.cmdb.system.ha import HaSC
from fortigate_api.cmdb.system.ha_monitor import HaMonitorSC
from fortigate_api.cmdb.system.interface import InterfaceSC
from fortigate_api.cmdb.system.ipip_tunnel import IpipTunnelSC
from fortigate_api.cmdb.system.ips import IpsSC
from fortigate_api.cmdb.system.ips_urlfilter_dns import IpsUrlfilterDnsSC
from fortigate_api.cmdb.system.ips_urlfilter_dns6 import IpsUrlfilterDns6SC
from fortigate_api.cmdb.system.ipsec_aggregate import IpsecAggregateSC
from fortigate_api.cmdb.system.ipv6_neighbor_cache import Ipv6NeighborCacheSC
from fortigate_api.cmdb.system.ipv6_tunnel import Ipv6TunnelSC
from fortigate_api.cmdb.system.link_monitor import LinkMonitorSC
from fortigate_api.cmdb.system.lte_modem import LteModemSC
from fortigate_api.cmdb.system.mac_address_table import MacAddressTableSC
from fortigate_api.cmdb.system.mobile_tunnel import MobileTunnelSC
from fortigate_api.cmdb.system.modem import ModemSC
from fortigate_api.cmdb.system.nat64 import Nat64SC
from fortigate_api.cmdb.system.nd_proxy import NdProxySC
from fortigate_api.cmdb.system.netflow import NetflowSC
from fortigate_api.cmdb.system.network_visibility import NetworkVisibilitySC
from fortigate_api.cmdb.system.npu import NpuSC
from fortigate_api.cmdb.system.ntp import NtpSC
from fortigate_api.cmdb.system.object_tagging import ObjectTaggingSC
from fortigate_api.cmdb.system.password_policy import PasswordPolicySC
from fortigate_api.cmdb.system.password_policy_guest_admin import PasswordPolicyGuestAdminSC
from fortigate_api.cmdb.system.physical_switch import PhysicalSwitchSC
from fortigate_api.cmdb.system.pppoe_interface import PppoeInterfaceSC
from fortigate_api.cmdb.system.probe_response import ProbeResponseSC
from fortigate_api.cmdb.system.proxy_arp import ProxyArpSC
from fortigate_api.cmdb.system.ptp import PtpSC
from fortigate_api.cmdb.system.replacemsg_group import ReplacemsgGroupSC
from fortigate_api.cmdb.system.replacemsg_image import ReplacemsgImageSC
from fortigate_api.cmdb.system.resource_limits import ResourceLimitsSC
from fortigate_api.cmdb.system.saml import SamlSC
from fortigate_api.cmdb.system.sdn_connector import SdnConnectorSC
from fortigate_api.cmdb.system.sdwan import SdwanSC
from fortigate_api.cmdb.system.session_helper import SessionHelperSC
from fortigate_api.cmdb.system.session_ttl import SessionTtlSC
from fortigate_api.cmdb.system.settings import SettingsSC
from fortigate_api.cmdb.system.sflow import SflowSC
from fortigate_api.cmdb.system.sit_tunnel import SitTunnelSC
from fortigate_api.cmdb.system.sms_server import SmsServerSC
from fortigate_api.cmdb.system.speed_test_server import SpeedTestServerSC
from fortigate_api.cmdb.system.sso_admin import SsoAdminSC
from fortigate_api.cmdb.system.standalone_cluster import StandaloneClusterSC
from fortigate_api.cmdb.system.storage import StorageSC
from fortigate_api.cmdb.system.stp import StpSC
from fortigate_api.cmdb.system.switch_interface import SwitchInterfaceSC
from fortigate_api.cmdb.system.tos_based_priority import TosBasedPrioritySC
from fortigate_api.cmdb.system.vdom import VdomSC
from fortigate_api.cmdb.system.vdom_dns import VdomDnsSC
from fortigate_api.cmdb.system.vdom_exception import VdomExceptionSC
from fortigate_api.cmdb.system.vdom_link import VdomLinkSC
from fortigate_api.cmdb.system.vdom_netflow import VdomNetflowSC
from fortigate_api.cmdb.system.vdom_property import VdomPropertySC
from fortigate_api.cmdb.system.vdom_radius_server import VdomRadiusServerSC
from fortigate_api.cmdb.system.vdom_sflow import VdomSflowSC
from fortigate_api.cmdb.system.virtual_switch import VirtualSwitchSC
from fortigate_api.cmdb.system.virtual_wire_pair import VirtualWirePairSC
from fortigate_api.cmdb.system.vne_tunnel import VneTunnelSC
from fortigate_api.cmdb.system.vxlan import VxlanSC
from fortigate_api.cmdb.system.wccp import WccpSC
from fortigate_api.cmdb.system.zone import ZoneSC
from fortigate_api.fortigate import FortiGate


class SystemC:
    """Cmdb/system connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init SystemC."""

        self.accprofile = AccprofileSC(fortigate, **kwargs)
        """:py:class:`.AccprofileSC` cmdb/system/accprofile."""

        self.admin = AdminSC(fortigate, **kwargs)
        """:py:class:`.AdminSC` cmdb/system/admin."""

        self.alarm = AlarmSC(fortigate, **kwargs)
        """:py:class:`.AlarmSC` cmdb/system/alarm."""

        self.api_user = ApiUserSC(fortigate, **kwargs)
        """:py:class:`.ApiUserSC` cmdb/system/api-user."""

        self.arp_table = ArpTableSC(fortigate, **kwargs)
        """:py:class:`.ArpTableSC` cmdb/system/arp-table."""

        self.auto_install = AutoInstallSC(fortigate, **kwargs)
        """:py:class:`.AutoInstallSC` cmdb/system/auto-install."""

        self.auto_script = AutoScriptSC(fortigate, **kwargs)
        """:py:class:`.AutoScriptSC` cmdb/system/auto-script."""

        self.automation_action = AutomationActionSC(fortigate, **kwargs)
        """:py:class:`.AutomationActionSC` cmdb/system/automation-action."""

        self.automation_destination = AutomationDestinationSC(fortigate, **kwargs)
        """:py:class:`.AutomationDestinationSC` cmdb/system/automation-destination."""

        self.automation_stitch = AutomationStitchSC(fortigate, **kwargs)
        """:py:class:`.AutomationStitchSC` cmdb/system/automation-stitch."""

        self.automation_trigger = AutomationTriggerSC(fortigate, **kwargs)
        """:py:class:`.AutomationTriggerSC` cmdb/system/automation-trigger."""

        self.central_management = CentralManagementSC(fortigate, **kwargs)
        """:py:class:`.CentralManagementSC` cmdb/system/central-management."""

        self.cluster_sync = ClusterSyncSC(fortigate, **kwargs)
        """:py:class:`.ClusterSyncSC` cmdb/system/cluster-sync."""

        self.console = ConsoleSC(fortigate, **kwargs)
        """:py:class:`.ConsoleSC` cmdb/system/console."""

        self.csf = CsfSC(fortigate, **kwargs)
        """:py:class:`.CsfSC` cmdb/system/csf."""

        self.custom_language = CustomLanguageSC(fortigate, **kwargs)
        """:py:class:`.CustomLanguageSC` cmdb/system/custom-language."""

        self.ddns = DdnsSC(fortigate, **kwargs)
        """:py:class:`.DdnsSC` cmdb/system/ddns."""

        self.dedicated_mgmt = DedicatedMgmtSC(fortigate, **kwargs)
        """:py:class:`.DedicatedMgmtSC` cmdb/system/dedicated-mgmt."""

        self.dns = DnsSC(fortigate, **kwargs)
        """:py:class:`.DnsSC` cmdb/system/dns."""

        self.dns_database = DnsDatabaseSC(fortigate, **kwargs)
        """:py:class:`.DnsDatabaseSC` cmdb/system/dns-database."""

        self.dns_server = DnsServerSC(fortigate, **kwargs)
        """:py:class:`.DnsServerSC` cmdb/system/dns-server."""

        self.dscp_based_priority = DscpBasedPrioritySC(fortigate, **kwargs)
        """:py:class:`.DscpBasedPrioritySC` cmdb/system/dscp-based-priority."""

        self.email_server = EmailServerSC(fortigate, **kwargs)
        """:py:class:`.EmailServerSC` cmdb/system/email-server."""

        self.external_resource = ExternalResourceSC(fortigate, **kwargs)
        """:py:class:`.ExternalResourceSC` cmdb/system/external-resource."""

        self.fips_cc = FipsCcSC(fortigate, **kwargs)
        """:py:class:`.FipsCcSC` cmdb/system/fips-cc."""

        self.fortiguard = FortiguardSC(fortigate, **kwargs)
        """:py:class:`.FortiguardSC` cmdb/system/fortiguard."""

        self.fortimanager = FortimanagerSC(fortigate, **kwargs)
        """:py:class:`.FortimanagerSC` cmdb/system/fortimanager."""

        self.fortisandbox = FortisandboxSC(fortigate, **kwargs)
        """:py:class:`.FortisandboxSC` cmdb/system/fortisandbox."""

        self.fsso_polling = FssoPollingSC(fortigate, **kwargs)
        """:py:class:`.FssoPollingSC` cmdb/system/fsso-polling."""

        self.ftm_push = FtmPushSC(fortigate, **kwargs)
        """:py:class:`.FtmPushSC` cmdb/system/ftm-push."""

        self.geneve = GeneveSC(fortigate, **kwargs)
        """:py:class:`.GeneveSC` cmdb/system/geneve."""

        self.geoip_country = GeoipCountrySC(fortigate, **kwargs)
        """:py:class:`.GeoipCountrySC` cmdb/system/geoip-country."""

        self.geoip_override = GeoipOverrideSC(fortigate, **kwargs)
        """:py:class:`.GeoipOverrideSC` cmdb/system/geoip-override."""

        self.global_ = GlobalSC(fortigate, **kwargs)
        """:py:class:`.GlobalSC` cmdb/system/global."""

        self.gre_tunnel = GreTunnelSC(fortigate, **kwargs)
        """:py:class:`.GreTunnelSC` cmdb/system/gre-tunnel."""

        self.ha = HaSC(fortigate, **kwargs)
        """:py:class:`.HaSC` cmdb/system/ha."""

        self.ha_monitor = HaMonitorSC(fortigate, **kwargs)
        """:py:class:`.HaMonitorSC` cmdb/system/ha-monitor."""

        self.interface = InterfaceSC(fortigate, **kwargs)
        """:py:class:`.InterfaceSC` cmdb/system/interface."""

        self.ipip_tunnel = IpipTunnelSC(fortigate, **kwargs)
        """:py:class:`.IpipTunnelSC` cmdb/system/ipip-tunnel."""

        self.ips = IpsSC(fortigate, **kwargs)
        """:py:class:`.IpsSC` cmdb/system/ips."""

        self.ips_urlfilter_dns = IpsUrlfilterDnsSC(fortigate, **kwargs)
        """:py:class:`.IpsUrlfilterDnsSC` cmdb/system/ips-urlfilter-dns."""

        self.ips_urlfilter_dns6 = IpsUrlfilterDns6SC(fortigate, **kwargs)
        """:py:class:`.IpsUrlfilterDns6SC` cmdb/system/ips-urlfilter-dns6."""

        self.ipsec_aggregate = IpsecAggregateSC(fortigate, **kwargs)
        """:py:class:`.IpsecAggregateSC` cmdb/system/ipsec-aggregate."""

        self.ipv6_neighbor_cache = Ipv6NeighborCacheSC(fortigate, **kwargs)
        """:py:class:`.Ipv6NeighborCacheSC` cmdb/system/ipv6-neighbor-cache."""

        self.ipv6_tunnel = Ipv6TunnelSC(fortigate, **kwargs)
        """:py:class:`.Ipv6TunnelSC` cmdb/system/ipv6-tunnel."""

        self.link_monitor = LinkMonitorSC(fortigate, **kwargs)
        """:py:class:`.LinkMonitorSC` cmdb/system/link-monitor."""

        self.lte_modem = LteModemSC(fortigate, **kwargs)
        """:py:class:`.LteModemSC` cmdb/system/lte-modem."""

        self.mac_address_table = MacAddressTableSC(fortigate, **kwargs)
        """:py:class:`.MacAddressTableSC` cmdb/system/mac-address-table."""

        self.mobile_tunnel = MobileTunnelSC(fortigate, **kwargs)
        """:py:class:`.MobileTunnelSC` cmdb/system/mobile-tunnel."""

        self.modem = ModemSC(fortigate, **kwargs)
        """:py:class:`.ModemSC` cmdb/system/modem."""

        self.nat64 = Nat64SC(fortigate, **kwargs)
        """:py:class:`.Nat64SC` cmdb/system/nat64."""

        self.nd_proxy = NdProxySC(fortigate, **kwargs)
        """:py:class:`.NdProxySC` cmdb/system/nd-proxy."""

        self.netflow = NetflowSC(fortigate, **kwargs)
        """:py:class:`.NetflowSC` cmdb/system/netflow."""

        self.network_visibility = NetworkVisibilitySC(fortigate, **kwargs)
        """:py:class:`.NetworkVisibilitySC` cmdb/system/network-visibility."""

        self.npu = NpuSC(fortigate, **kwargs)
        """:py:class:`.NpuSC` cmdb/system/npu."""

        self.ntp = NtpSC(fortigate, **kwargs)
        """:py:class:`.NtpSC` cmdb/system/ntp."""

        self.object_tagging = ObjectTaggingSC(fortigate, **kwargs)
        """:py:class:`.ObjectTaggingSC` cmdb/system/object-tagging."""

        self.password_policy = PasswordPolicySC(fortigate, **kwargs)
        """:py:class:`.PasswordPolicySC` cmdb/system/password-policy."""

        self.password_policy_guest_admin = PasswordPolicyGuestAdminSC(fortigate, **kwargs)
        """:py:class:`.PasswordPolicyGuestAdminSC` cmdb/system/password-policy-guest-admin."""

        self.physical_switch = PhysicalSwitchSC(fortigate, **kwargs)
        """:py:class:`.PhysicalSwitchSC` cmdb/system/physical-switch."""

        self.pppoe_interface = PppoeInterfaceSC(fortigate, **kwargs)
        """:py:class:`.PppoeInterfaceSC` cmdb/system/pppoe-interface."""

        self.probe_response = ProbeResponseSC(fortigate, **kwargs)
        """:py:class:`.ProbeResponseSC` cmdb/system/probe-response."""

        self.proxy_arp = ProxyArpSC(fortigate, **kwargs)
        """:py:class:`.ProxyArpSC` cmdb/system/proxy-arp."""

        self.ptp = PtpSC(fortigate, **kwargs)
        """:py:class:`.PtpSC` cmdb/system/ptp."""

        self.replacemsg_group = ReplacemsgGroupSC(fortigate, **kwargs)
        """:py:class:`.ReplacemsgGroupSC` cmdb/system/replacemsg-group."""

        self.replacemsg_image = ReplacemsgImageSC(fortigate, **kwargs)
        """:py:class:`.ReplacemsgImageSC` cmdb/system/replacemsg-image."""

        self.resource_limits = ResourceLimitsSC(fortigate, **kwargs)
        """:py:class:`.ResourceLimitsSC` cmdb/system/resource-limits."""

        self.saml = SamlSC(fortigate, **kwargs)
        """:py:class:`.SamlSC` cmdb/system/saml."""

        self.sdn_connector = SdnConnectorSC(fortigate, **kwargs)
        """:py:class:`.SdnConnectorSC` cmdb/system/sdn-connector."""

        self.sdwan = SdwanSC(fortigate, **kwargs)
        """:py:class:`.SdwanSC` cmdb/system/sdwan."""

        self.session_helper = SessionHelperSC(fortigate, **kwargs)
        """:py:class:`.SessionHelperSC` cmdb/system/session-helper."""

        self.session_ttl = SessionTtlSC(fortigate, **kwargs)
        """:py:class:`.SessionTtlSC` cmdb/system/session-ttl."""

        self.settings = SettingsSC(fortigate, **kwargs)
        """:py:class:`.SettingsSC` cmdb/system/settings."""

        self.sflow = SflowSC(fortigate, **kwargs)
        """:py:class:`.SflowSC` cmdb/system/sflow."""

        self.sit_tunnel = SitTunnelSC(fortigate, **kwargs)
        """:py:class:`.SitTunnelSC` cmdb/system/sit-tunnel."""

        self.sms_server = SmsServerSC(fortigate, **kwargs)
        """:py:class:`.SmsServerSC` cmdb/system/sms-server."""

        self.speed_test_server = SpeedTestServerSC(fortigate, **kwargs)
        """:py:class:`.SpeedTestServerSC` cmdb/system/speed-test-server."""

        self.sso_admin = SsoAdminSC(fortigate, **kwargs)
        """:py:class:`.SsoAdminSC` cmdb/system/sso-admin."""

        self.standalone_cluster = StandaloneClusterSC(fortigate, **kwargs)
        """:py:class:`.StandaloneClusterSC` cmdb/system/standalone-cluster."""

        self.storage = StorageSC(fortigate, **kwargs)
        """:py:class:`.StorageSC` cmdb/system/storage."""

        self.stp = StpSC(fortigate, **kwargs)
        """:py:class:`.StpSC` cmdb/system/stp."""

        self.switch_interface = SwitchInterfaceSC(fortigate, **kwargs)
        """:py:class:`.SwitchInterfaceSC` cmdb/system/switch-interface."""

        self.tos_based_priority = TosBasedPrioritySC(fortigate, **kwargs)
        """:py:class:`.TosBasedPrioritySC` cmdb/system/tos-based-priority."""

        self.vdom = VdomSC(fortigate, **kwargs)
        """:py:class:`.VdomSC` cmdb/system/vdom."""

        self.vdom_dns = VdomDnsSC(fortigate, **kwargs)
        """:py:class:`.VdomDnsSC` cmdb/system/vdom-dns."""

        self.vdom_exception = VdomExceptionSC(fortigate, **kwargs)
        """:py:class:`.VdomExceptionSC` cmdb/system/vdom-exception."""

        self.vdom_link = VdomLinkSC(fortigate, **kwargs)
        """:py:class:`.VdomLinkSC` cmdb/system/vdom-link."""

        self.vdom_netflow = VdomNetflowSC(fortigate, **kwargs)
        """:py:class:`.VdomNetflowSC` cmdb/system/vdom-netflow."""

        self.vdom_property = VdomPropertySC(fortigate, **kwargs)
        """:py:class:`.VdomPropertySC` cmdb/system/vdom-property."""

        self.vdom_radius_server = VdomRadiusServerSC(fortigate, **kwargs)
        """:py:class:`.VdomRadiusServerSC` cmdb/system/vdom-radius-server."""

        self.vdom_sflow = VdomSflowSC(fortigate, **kwargs)
        """:py:class:`.VdomSflowSC` cmdb/system/vdom-sflow."""

        self.virtual_switch = VirtualSwitchSC(fortigate, **kwargs)
        """:py:class:`.VirtualSwitchSC` cmdb/system/virtual-switch."""

        self.virtual_wire_pair = VirtualWirePairSC(fortigate, **kwargs)
        """:py:class:`.VirtualWirePairSC` cmdb/system/virtual-wire-pair."""

        self.vne_tunnel = VneTunnelSC(fortigate, **kwargs)
        """:py:class:`.VneTunnelSC` cmdb/system/vne-tunnel."""

        self.vxlan = VxlanSC(fortigate, **kwargs)
        """:py:class:`.VxlanSC` cmdb/system/vxlan."""

        self.wccp = WccpSC(fortigate, **kwargs)
        """:py:class:`.WccpSC` cmdb/system/wccp."""

        self.zone = ZoneSC(fortigate, **kwargs)
        """:py:class:`.ZoneSC` cmdb/system/zone."""
