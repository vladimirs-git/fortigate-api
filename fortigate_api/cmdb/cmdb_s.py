"""Cmdb scope connectors."""

from fortigate_api.cmdb.alertemail.alertemail_c import AlertemailC
from fortigate_api.cmdb.antivirus.antivirus_c import AntivirusC
from fortigate_api.cmdb.application.application_c import ApplicationC
from fortigate_api.cmdb.authentication.authentication_c import AuthenticationC
from fortigate_api.cmdb.certificate.certificate_c import CertificateC
from fortigate_api.cmdb.credential_store.credential_store_c import CredentialStoreC
from fortigate_api.cmdb.dlp.dlp_c import DlpC
from fortigate_api.cmdb.dnsfilter.dnsfilter_c import DnsfilterC
from fortigate_api.cmdb.emailfilter.emailfilter_c import EmailfilterC
from fortigate_api.cmdb.endpoint_control.endpoint_control_c import EndpointControlC
from fortigate_api.cmdb.extender_controller.extender_controller_c import ExtenderControllerC
from fortigate_api.cmdb.file_filter.file_filter_c import FileFilterC
from fortigate_api.cmdb.firewall.firewall_c import FirewallC
from fortigate_api.cmdb.firewall_ipmacbinding.firewall_ipmacbinding_c import FirewallIpmacbindingC
from fortigate_api.cmdb.firewall_schedule.firewall_schedule_c import FirewallScheduleC
from fortigate_api.cmdb.firewall_service.firewall_service_c import FirewallServiceC
from fortigate_api.cmdb.firewall_shaper.firewall_shaper_c import FirewallShaperC
from fortigate_api.cmdb.firewall_ssh.firewall_ssh_c import FirewallSshC
from fortigate_api.cmdb.firewall_ssl.firewall_ssl_c import FirewallSslC
from fortigate_api.cmdb.firewall_wildcard_fqdn.firewall_wildcard_fqdn_c import FirewallWildcardFqdnC
from fortigate_api.cmdb.ftp_proxy.ftp_proxy_c import FtpProxyC
from fortigate_api.cmdb.icap.icap_c import IcapC
from fortigate_api.cmdb.ips.ips_c import IpsC
from fortigate_api.cmdb.log.log_c import LogC
from fortigate_api.cmdb.log_disk.log_disk_c import LogDiskC
from fortigate_api.cmdb.log_fortianalyzer.log_fortianalyzer_c import LogFortianalyzerC
from fortigate_api.cmdb.log_fortianalyzer2.log_fortianalyzer2_c import LogFortianalyzer2C
from fortigate_api.cmdb.log_fortianalyzer3.log_fortianalyzer3_c import LogFortianalyzer3C
from fortigate_api.cmdb.log_fortianalyzer_cloud.log_fortianalyzer_cloud_c import (
    LogFortianalyzerCloudC,
)
from fortigate_api.cmdb.log_fortiguard.log_fortiguard_c import LogFortiguardC
from fortigate_api.cmdb.log_memory.log_memory_c import LogMemoryC
from fortigate_api.cmdb.log_null_device.log_null_device_c import LogNullDeviceC
from fortigate_api.cmdb.log_syslogd.log_syslogd_c import LogSyslogdC
from fortigate_api.cmdb.log_syslogd2.log_syslogd2_c import LogSyslogd2C
from fortigate_api.cmdb.log_syslogd3.log_syslogd3_c import LogSyslogd3C
from fortigate_api.cmdb.log_syslogd4.log_syslogd4_c import LogSyslogd4C
from fortigate_api.cmdb.log_webtrends.log_webtrends_c import LogWebtrendsC
from fortigate_api.cmdb.report.report_c import ReportC
from fortigate_api.cmdb.router.router_c import RouterC
from fortigate_api.cmdb.ssh_filter.ssh_filter_c import SshFilterC
from fortigate_api.cmdb.switch_controller.switch_controller_c import SwitchControllerC
from fortigate_api.cmdb.switch_controller_auto_config.switch_controller_auto_config_c import (
    SwitchControllerAutoConfigC,
)
from fortigate_api.cmdb.switch_controller_initial_config.switch_controller_initial_config_c import (
    SwitchControllerInitialConfigC,
)
from fortigate_api.cmdb.switch_controller_security_policy.switch_controller_security_policy_c import (
    SwitchControllerSecurityPolicyC,
)
from fortigate_api.cmdb.system.system_c import SystemC
from fortigate_api.cmdb.system_3g_modem.system_3g_modem_c import System3gModemC
from fortigate_api.cmdb.system_autoupdate.system_autoupdate_c import SystemAutoupdateC
from fortigate_api.cmdb.system_dhcp.system_dhcp_c import SystemDhcpC
from fortigate_api.cmdb.system_dhcp6.system_dhcp6_c import SystemDhcp6C
from fortigate_api.cmdb.system_lldp.system_lldp_c import SystemLldpC
from fortigate_api.cmdb.system_replacemsg.system_replacemsg_c import SystemReplacemsgC
from fortigate_api.cmdb.system_snmp.system_snmp_c import SystemSnmpC
from fortigate_api.cmdb.user.user_c import UserC
from fortigate_api.cmdb.voip.voip_c import VoipC
from fortigate_api.cmdb.vpn.vpn_c import VpnC
from fortigate_api.cmdb.vpn_certificate.vpn_certificate_c import VpnCertificateC
from fortigate_api.cmdb.vpn_ipsec.vpn_ipsec_c import VpnIpsecC
from fortigate_api.cmdb.vpn_ssl.vpn_ssl_c import VpnSslC
from fortigate_api.cmdb.vpn_ssl_web.vpn_ssl_web_c import VpnSslWebC
from fortigate_api.cmdb.waf.waf_c import WafC
from fortigate_api.cmdb.wanopt.wanopt_c import WanoptC
from fortigate_api.cmdb.web_proxy.web_proxy_c import WebProxyC
from fortigate_api.cmdb.webfilter.webfilter_c import WebfilterC
from fortigate_api.cmdb.wireless_controller.wireless_controller_c import WirelessControllerC
from fortigate_api.cmdb.wireless_controller_hotspot20.wireless_controller_hotspot20_c import (
    WirelessControllerHotspot20C,
)
from fortigate_api.fortigate import FortiGate


class CmdbS:
    """Cmdb scope connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init CmdbS."""

        self.alertemail = AlertemailC(fortigate, **kwargs)
        """:py:class:`.AlertemailC` cmdb/alertemail connectors."""

        self.antivirus = AntivirusC(fortigate, **kwargs)
        """:py:class:`.AntivirusC` cmdb/antivirus connectors."""

        self.application = ApplicationC(fortigate, **kwargs)
        """:py:class:`.ApplicationC` cmdb/application connectors."""

        self.authentication = AuthenticationC(fortigate, **kwargs)
        """:py:class:`.AuthenticationC` cmdb/authentication connectors."""

        self.certificate = CertificateC(fortigate, **kwargs)
        """:py:class:`.CertificateC` cmdb/certificate connectors."""

        self.credential_store = CredentialStoreC(fortigate, **kwargs)
        """:py:class:`.CredentialStoreC` cmdb/credential-store connectors."""

        self.dlp = DlpC(fortigate, **kwargs)
        """:py:class:`.DlpC` cmdb/dlp connectors."""

        self.dnsfilter = DnsfilterC(fortigate, **kwargs)
        """:py:class:`.DnsfilterC` cmdb/dnsfilter connectors."""

        self.emailfilter = EmailfilterC(fortigate, **kwargs)
        """:py:class:`.EmailfilterC` cmdb/emailfilter connectors."""

        self.endpoint_control = EndpointControlC(fortigate, **kwargs)
        """:py:class:`.EndpointControlC` cmdb/endpoint-control connectors."""

        self.extender_controller = ExtenderControllerC(fortigate, **kwargs)
        """:py:class:`.ExtenderControllerC` cmdb/extender-controller connectors."""

        self.file_filter = FileFilterC(fortigate, **kwargs)
        """:py:class:`.FileFilterC` cmdb/file-filter connectors."""

        self.firewall = FirewallC(fortigate, **kwargs)
        """:py:class:`.FirewallC` cmdb/firewall connectors."""

        self.firewall_ipmacbinding = FirewallIpmacbindingC(fortigate, **kwargs)
        """:py:class:`.FirewallIpmacbindingC` cmdb/firewall.ipmacbinding connectors."""

        self.firewall_schedule = FirewallScheduleC(fortigate, **kwargs)
        """:py:class:`.FirewallScheduleC` cmdb/firewall.schedule connectors."""

        self.firewall_service = FirewallServiceC(fortigate, **kwargs)
        """:py:class:`.FirewallServiceC` cmdb/firewall.service connectors."""

        self.firewall_shaper = FirewallShaperC(fortigate, **kwargs)
        """:py:class:`.FirewallShaperC` cmdb/firewall.shaper connectors."""

        self.firewall_ssh = FirewallSshC(fortigate, **kwargs)
        """:py:class:`.FirewallSshC` cmdb/firewall.ssh connectors."""

        self.firewall_ssl = FirewallSslC(fortigate, **kwargs)
        """:py:class:`.FirewallSslC` cmdb/firewall.ssl connectors."""

        self.firewall_wildcard_fqdn = FirewallWildcardFqdnC(fortigate, **kwargs)
        """:py:class:`.FirewallWildcardFqdnC` cmdb/firewall.wildcard-fqdn connectors."""

        self.ftp_proxy = FtpProxyC(fortigate, **kwargs)
        """:py:class:`.FtpProxyC` cmdb/ftp-proxy connectors."""

        self.icap = IcapC(fortigate, **kwargs)
        """:py:class:`.IcapC` cmdb/icap connectors."""

        self.ips = IpsC(fortigate, **kwargs)
        """:py:class:`.IpsC` cmdb/ips connectors."""

        self.log = LogC(fortigate, **kwargs)
        """:py:class:`.LogC` cmdb/log connectors."""

        self.log_disk = LogDiskC(fortigate, **kwargs)
        """:py:class:`.LogDiskC` cmdb/log.disk connectors."""

        self.log_fortianalyzer = LogFortianalyzerC(fortigate, **kwargs)
        """:py:class:`.LogFortianalyzerC` cmdb/log.fortianalyzer connectors."""

        self.log_fortianalyzer2 = LogFortianalyzer2C(fortigate, **kwargs)
        """:py:class:`.LogFortianalyzer2C` cmdb/log.fortianalyzer2 connectors."""

        self.log_fortianalyzer3 = LogFortianalyzer3C(fortigate, **kwargs)
        """:py:class:`.LogFortianalyzer3C` cmdb/log.fortianalyzer3 connectors."""

        self.log_fortianalyzer_cloud = LogFortianalyzerCloudC(fortigate, **kwargs)
        """:py:class:`.LogFortianalyzerCloudC` cmdb/log.fortianalyzer-cloud connectors."""

        self.log_fortiguard = LogFortiguardC(fortigate, **kwargs)
        """:py:class:`.LogFortiguardC` cmdb/log.fortiguard connectors."""

        self.log_memory = LogMemoryC(fortigate, **kwargs)
        """:py:class:`.LogMemoryC` cmdb/log.memory connectors."""

        self.log_null_device = LogNullDeviceC(fortigate, **kwargs)
        """:py:class:`.LogNullDeviceC` cmdb/log.null-device connectors."""

        self.log_syslogd = LogSyslogdC(fortigate, **kwargs)
        """:py:class:`.LogSyslogdC` cmdb/log.syslogd connectors."""

        self.log_syslogd2 = LogSyslogd2C(fortigate, **kwargs)
        """:py:class:`.LogSyslogd2C` cmdb/log.syslogd2 connectors."""

        self.log_syslogd3 = LogSyslogd3C(fortigate, **kwargs)
        """:py:class:`.LogSyslogd3C` cmdb/log.syslogd3 connectors."""

        self.log_syslogd4 = LogSyslogd4C(fortigate, **kwargs)
        """:py:class:`.LogSyslogd4C` cmdb/log.syslogd4 connectors."""

        self.log_webtrends = LogWebtrendsC(fortigate, **kwargs)
        """:py:class:`.LogWebtrendsC` cmdb/log.webtrends connectors."""

        self.report = ReportC(fortigate, **kwargs)
        """:py:class:`.ReportC` cmdb/report connectors."""

        self.router = RouterC(fortigate, **kwargs)
        """:py:class:`.RouterC` cmdb/router connectors."""

        self.ssh_filter = SshFilterC(fortigate, **kwargs)
        """:py:class:`.SshFilterC` cmdb/ssh-filter connectors."""

        self.switch_controller = SwitchControllerC(fortigate, **kwargs)
        """:py:class:`.SwitchControllerC` cmdb/switch-controller connectors."""

        self.switch_controller_auto_config = SwitchControllerAutoConfigC(fortigate, **kwargs)
        """:py:class:`.SwitchControllerAutoConfigC` cmdb/switch-controller.auto-config connectors."""

        self.switch_controller_initial_config = SwitchControllerInitialConfigC(fortigate, **kwargs)
        """:py:class:`.SwitchControllerInitialConfigC` cmdb/switch-controller.initial-config connectors."""

        self.switch_controller_security_policy = SwitchControllerSecurityPolicyC(
            fortigate, **kwargs
        )
        """:py:class:`.SwitchControllerSecurityPolicyC` cmdb/switch-controller.security-policy connectors."""

        self.system = SystemC(fortigate, **kwargs)
        """:py:class:`.SystemC` cmdb/system connectors."""

        self.system_3g_modem = System3gModemC(fortigate, **kwargs)
        """:py:class:`.System3gModemC` cmdb/system.3g-modem connectors."""

        self.system_autoupdate = SystemAutoupdateC(fortigate, **kwargs)
        """:py:class:`.SystemAutoupdateC` cmdb/system.autoupdate connectors."""

        self.system_dhcp = SystemDhcpC(fortigate, **kwargs)
        """:py:class:`.SystemDhcpC` cmdb/system.dhcp connectors."""

        self.system_dhcp6 = SystemDhcp6C(fortigate, **kwargs)
        """:py:class:`.SystemDhcp6C` cmdb/system.dhcp6 connectors."""

        self.system_lldp = SystemLldpC(fortigate, **kwargs)
        """:py:class:`.SystemLldpC` cmdb/system.lldp connectors."""

        self.system_replacemsg = SystemReplacemsgC(fortigate, **kwargs)
        """:py:class:`.SystemReplacemsgC` cmdb/system.replacemsg connectors."""

        self.system_snmp = SystemSnmpC(fortigate, **kwargs)
        """:py:class:`.SystemSnmpC` cmdb/system.snmp connectors."""

        self.user = UserC(fortigate, **kwargs)
        """:py:class:`.UserC` cmdb/user connectors."""

        self.voip = VoipC(fortigate, **kwargs)
        """:py:class:`.VoipC` cmdb/voip connectors."""

        self.vpn = VpnC(fortigate, **kwargs)
        """:py:class:`.VpnC` cmdb/vpn connectors."""

        self.vpn_certificate = VpnCertificateC(fortigate, **kwargs)
        """:py:class:`.VpnCertificateC` cmdb/vpn.certificate connectors."""

        self.vpn_ipsec = VpnIpsecC(fortigate, **kwargs)
        """:py:class:`.VpnIpsecC` cmdb/vpn.ipsec connectors."""

        self.vpn_ssl = VpnSslC(fortigate, **kwargs)
        """:py:class:`.VpnSslC` cmdb/vpn.ssl connectors."""

        self.vpn_ssl_web = VpnSslWebC(fortigate, **kwargs)
        """:py:class:`.VpnSslWebC` cmdb/vpn.ssl.web connectors."""

        self.waf = WafC(fortigate, **kwargs)
        """:py:class:`.WafC` cmdb/waf connectors."""

        self.wanopt = WanoptC(fortigate, **kwargs)
        """:py:class:`.WanoptC` cmdb/wanopt connectors."""

        self.web_proxy = WebProxyC(fortigate, **kwargs)
        """:py:class:`.WebProxyC` cmdb/web-proxy connectors."""

        self.webfilter = WebfilterC(fortigate, **kwargs)
        """:py:class:`.WebfilterC` cmdb/webfilter connectors."""

        self.wireless_controller = WirelessControllerC(fortigate, **kwargs)
        """:py:class:`.WirelessControllerC` cmdb/wireless-controller connectors."""

        self.wireless_controller_hotspot20 = WirelessControllerHotspot20C(fortigate, **kwargs)
        """:py:class:`.WirelessControllerHotspot20C` cmdb/wireless-controller.hotspot20 connectors."""
