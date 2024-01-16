"""Cmdb scope connectors."""

from fortigate_api.cmdb.alertemail.alertemail_c import AlertemailC
from fortigate_api.cmdb.antivirus.antivirus_c import AntivirusC
from fortigate_api.cmdb.application.application_c import ApplicationC
from fortigate_api.cmdb.authentication.authentication_c import AuthenticationC
from fortigate_api.cmdb.certificate.certificate_c import CertificateC
from fortigate_api.cmdb.cmdb_s import CmdbS
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
