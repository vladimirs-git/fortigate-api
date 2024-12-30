"""Cmdb/firewall connectors."""

from fortigate_api.cmdb.firewall.acl import AclFC
from fortigate_api.cmdb.firewall.acl6 import Acl6FC
from fortigate_api.cmdb.firewall.address import AddressFC
from fortigate_api.cmdb.firewall.address6 import Address6FC
from fortigate_api.cmdb.firewall.address6_template import Address6TemplateFC
from fortigate_api.cmdb.firewall.addrgrp import AddrgrpFC
from fortigate_api.cmdb.firewall.addrgrp6 import Addrgrp6FC
from fortigate_api.cmdb.firewall.auth_portal import AuthPortalFC
from fortigate_api.cmdb.firewall.central_snat_map import CentralSnatMapFC
from fortigate_api.cmdb.firewall.city import CityFC
from fortigate_api.cmdb.firewall.country import CountryFC
from fortigate_api.cmdb.firewall.decrypted_traffic_mirror import DecryptedTrafficMirrorFC
from fortigate_api.cmdb.firewall.dnstranslation import DnstranslationFC
from fortigate_api.cmdb.firewall.dos_policy import DosPolicyFC
from fortigate_api.cmdb.firewall.dos_policy6 import DosPolicy6FC
from fortigate_api.cmdb.firewall.identity_based_route import IdentityBasedRouteFC
from fortigate_api.cmdb.firewall.interface_policy import InterfacePolicyFC
from fortigate_api.cmdb.firewall.interface_policy6 import InterfacePolicy6FC
from fortigate_api.cmdb.firewall.internet_service import InternetServiceFC
from fortigate_api.cmdb.firewall.internet_service_addition import InternetServiceAdditionFC
from fortigate_api.cmdb.firewall.internet_service_append import InternetServiceAppendFC
from fortigate_api.cmdb.firewall.internet_service_botnet import InternetServiceBotnetFC
from fortigate_api.cmdb.firewall.internet_service_custom import InternetServiceCustomFC
from fortigate_api.cmdb.firewall.internet_service_custom_group import InternetServiceCustomGroupFC
from fortigate_api.cmdb.firewall.internet_service_definition import InternetServiceDefinitionFC
from fortigate_api.cmdb.firewall.internet_service_extension import InternetServiceExtensionFC
from fortigate_api.cmdb.firewall.internet_service_group import InternetServiceGroupFC
from fortigate_api.cmdb.firewall.internet_service_ipbl_reason import InternetServiceIpblReasonFC
from fortigate_api.cmdb.firewall.internet_service_ipbl_vendor import InternetServiceIpblVendorFC
from fortigate_api.cmdb.firewall.internet_service_list import InternetServiceListFC
from fortigate_api.cmdb.firewall.internet_service_name import InternetServiceNameFC
from fortigate_api.cmdb.firewall.internet_service_owner import InternetServiceOwnerFC
from fortigate_api.cmdb.firewall.internet_service_reputation import InternetServiceReputationFC
from fortigate_api.cmdb.firewall.internet_service_sld import InternetServiceSldFC
from fortigate_api.cmdb.firewall.ip_translation import IpTranslationFC
from fortigate_api.cmdb.firewall.ippool import IppoolFC
from fortigate_api.cmdb.firewall.ippool6 import Ippool6FC
from fortigate_api.cmdb.firewall.ldb_monitor import LdbMonitorFC
from fortigate_api.cmdb.firewall.local_in_policy import LocalInPolicyFC
from fortigate_api.cmdb.firewall.local_in_policy6 import LocalInPolicy6FC
from fortigate_api.cmdb.firewall.multicast_address import MulticastAddressFC
from fortigate_api.cmdb.firewall.multicast_address6 import MulticastAddress6FC
from fortigate_api.cmdb.firewall.multicast_policy import MulticastPolicyFC
from fortigate_api.cmdb.firewall.multicast_policy6 import MulticastPolicy6FC
from fortigate_api.cmdb.firewall.policy import PolicyFC
from fortigate_api.cmdb.firewall.policy46 import Policy46FC
from fortigate_api.cmdb.firewall.policy64 import Policy64FC
from fortigate_api.cmdb.firewall.profile_group import ProfileGroupFC
from fortigate_api.cmdb.firewall.profile_protocol_options import ProfileProtocolOptionsFC
from fortigate_api.cmdb.firewall.proxy_address import ProxyAddressFC
from fortigate_api.cmdb.firewall.proxy_addrgrp import ProxyAddrgrpFC
from fortigate_api.cmdb.firewall.proxy_policy import ProxyPolicyFC
from fortigate_api.cmdb.firewall.region import RegionFC
from fortigate_api.cmdb.firewall.security_policy import SecurityPolicyFC
from fortigate_api.cmdb.firewall.shaping_policy import ShapingPolicyFC
from fortigate_api.cmdb.firewall.shaping_profile import ShapingProfileFC
from fortigate_api.cmdb.firewall.sniffer import SnifferFC
from fortigate_api.cmdb.firewall.ssl_server import SslServerFC
from fortigate_api.cmdb.firewall.ssl_ssh_profile import SslSshProfileFC
from fortigate_api.cmdb.firewall.traffic_class import TrafficClassFC
from fortigate_api.cmdb.firewall.ttl_policy import TtlPolicyFC
from fortigate_api.cmdb.firewall.vendor_mac import VendorMacFC
from fortigate_api.cmdb.firewall.vendor_mac_summary import VendorMacSummaryFC
from fortigate_api.cmdb.firewall.vip import VipFC
from fortigate_api.cmdb.firewall.vip46 import Vip46FC
from fortigate_api.cmdb.firewall.vip6 import Vip6FC
from fortigate_api.cmdb.firewall.vip64 import Vip64FC
from fortigate_api.cmdb.firewall.vipgrp import VipgrpFC
from fortigate_api.cmdb.firewall.vipgrp46 import Vipgrp46FC
from fortigate_api.cmdb.firewall.vipgrp6 import Vipgrp6FC
from fortigate_api.cmdb.firewall.vipgrp64 import Vipgrp64FC
from fortigate_api.fortigate import FortiGate


class FirewallC:
    """Cmdb/firewall connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init FirewallC."""
        self.dos_policy = DosPolicyFC(fortigate, **kwargs)
        """:py:class:`.DosPolicyFC` cmdb/firewall/DoS-policy."""

        self.dos_policy6 = DosPolicy6FC(fortigate, **kwargs)
        """:py:class:`.DosPolicy6FC` cmdb/firewall/DoS-policy6."""

        self.acl = AclFC(fortigate, **kwargs)
        """:py:class:`.AclFC` cmdb/firewall/acl."""

        self.acl6 = Acl6FC(fortigate, **kwargs)
        """:py:class:`.Acl6FC` cmdb/firewall/acl6."""

        self.address = AddressFC(fortigate, **kwargs)
        """:py:class:`.AddressFC` cmdb/firewall/address."""

        self.address6 = Address6FC(fortigate, **kwargs)
        """:py:class:`.Address6FC` cmdb/firewall/address6."""

        self.address6_template = Address6TemplateFC(fortigate, **kwargs)
        """:py:class:`.Address6TemplateFC` cmdb/firewall/address6-template."""

        self.addrgrp = AddrgrpFC(fortigate, **kwargs)
        """:py:class:`.AddrgrpFC` cmdb/firewall/addrgrp."""

        self.addrgrp6 = Addrgrp6FC(fortigate, **kwargs)
        """:py:class:`.Addrgrp6FC` cmdb/firewall/addrgrp6."""

        self.auth_portal = AuthPortalFC(fortigate, **kwargs)
        """:py:class:`.AuthPortalFC` cmdb/firewall/auth-portal."""

        self.central_snat_map = CentralSnatMapFC(fortigate, **kwargs)
        """:py:class:`.CentralSnatMapFC` cmdb/firewall/central-snat-map."""

        self.city = CityFC(fortigate, **kwargs)
        """:py:class:`.CityFC` cmdb/firewall/city."""

        self.country = CountryFC(fortigate, **kwargs)
        """:py:class:`.CountryFC` cmdb/firewall/country."""

        self.decrypted_traffic_mirror = DecryptedTrafficMirrorFC(fortigate, **kwargs)
        """:py:class:`.DecryptedTrafficMirrorFC` cmdb/firewall/decrypted-traffic-mirror."""

        self.dnstranslation = DnstranslationFC(fortigate, **kwargs)
        """:py:class:`.DnstranslationFC` cmdb/firewall/dnstranslation."""

        self.identity_based_route = IdentityBasedRouteFC(fortigate, **kwargs)
        """:py:class:`.IdentityBasedRouteFC` cmdb/firewall/identity-based-route."""

        self.interface_policy = InterfacePolicyFC(fortigate, **kwargs)
        """:py:class:`.InterfacePolicyFC` cmdb/firewall/interface-policy."""

        self.interface_policy6 = InterfacePolicy6FC(fortigate, **kwargs)
        """:py:class:`.InterfacePolicy6FC` cmdb/firewall/interface-policy6."""

        self.internet_service = InternetServiceFC(fortigate, **kwargs)
        """:py:class:`.InternetServiceFC` cmdb/firewall/internet-service."""

        self.internet_service_addition = InternetServiceAdditionFC(fortigate, **kwargs)
        """:py:class:`.InternetServiceAdditionFC` cmdb/firewall/internet-service-addition."""

        self.internet_service_append = InternetServiceAppendFC(fortigate, **kwargs)
        """:py:class:`.InternetServiceAppendFC` cmdb/firewall/internet-service-append."""

        self.internet_service_botnet = InternetServiceBotnetFC(fortigate, **kwargs)
        """:py:class:`.InternetServiceBotnetFC` cmdb/firewall/internet-service-botnet."""

        self.internet_service_custom = InternetServiceCustomFC(fortigate, **kwargs)
        """:py:class:`.InternetServiceCustomFC` cmdb/firewall/internet-service-custom."""

        self.internet_service_custom_group = InternetServiceCustomGroupFC(fortigate, **kwargs)
        """:py:class:`.InternetServiceCustomGroupFC` cmdb/firewall/internet-service-custom-group."""

        self.internet_service_definition = InternetServiceDefinitionFC(fortigate, **kwargs)
        """:py:class:`.InternetServiceDefinitionFC` cmdb/firewall/internet-service-definition."""

        self.internet_service_extension = InternetServiceExtensionFC(fortigate, **kwargs)
        """:py:class:`.InternetServiceExtensionFC` cmdb/firewall/internet-service-extension."""

        self.internet_service_group = InternetServiceGroupFC(fortigate, **kwargs)
        """:py:class:`.InternetServiceGroupFC` cmdb/firewall/internet-service-group."""

        self.internet_service_ipbl_reason = InternetServiceIpblReasonFC(fortigate, **kwargs)
        """:py:class:`.InternetServiceIpblReasonFC` cmdb/firewall/internet-service-ipbl-reason."""

        self.internet_service_ipbl_vendor = InternetServiceIpblVendorFC(fortigate, **kwargs)
        """:py:class:`.InternetServiceIpblVendorFC` cmdb/firewall/internet-service-ipbl-vendor."""

        self.internet_service_list = InternetServiceListFC(fortigate, **kwargs)
        """:py:class:`.InternetServiceListFC` cmdb/firewall/internet-service-list."""

        self.internet_service_name = InternetServiceNameFC(fortigate, **kwargs)
        """:py:class:`.InternetServiceNameFC` cmdb/firewall/internet-service-name."""

        self.internet_service_owner = InternetServiceOwnerFC(fortigate, **kwargs)
        """:py:class:`.InternetServiceOwnerFC` cmdb/firewall/internet-service-owner."""

        self.internet_service_reputation = InternetServiceReputationFC(fortigate, **kwargs)
        """:py:class:`.InternetServiceReputationFC` cmdb/firewall/internet-service-reputation."""

        self.internet_service_sld = InternetServiceSldFC(fortigate, **kwargs)
        """:py:class:`.InternetServiceSldFC` cmdb/firewall/internet-service-sld."""

        self.ip_translation = IpTranslationFC(fortigate, **kwargs)
        """:py:class:`.IpTranslationFC` cmdb/firewall/ip-translation."""

        self.ippool = IppoolFC(fortigate, **kwargs)
        """:py:class:`.IppoolFC` cmdb/firewall/ippool."""

        self.ippool6 = Ippool6FC(fortigate, **kwargs)
        """:py:class:`.Ippool6FC` cmdb/firewall/ippool6."""

        self.ldb_monitor = LdbMonitorFC(fortigate, **kwargs)
        """:py:class:`.LdbMonitorFC` cmdb/firewall/ldb-monitor."""

        self.local_in_policy = LocalInPolicyFC(fortigate, **kwargs)
        """:py:class:`.LocalInPolicyFC` cmdb/firewall/local-in-policy."""

        self.local_in_policy6 = LocalInPolicy6FC(fortigate, **kwargs)
        """:py:class:`.LocalInPolicy6FC` cmdb/firewall/local-in-policy6."""

        self.multicast_address = MulticastAddressFC(fortigate, **kwargs)
        """:py:class:`.MulticastAddressFC` cmdb/firewall/multicast-address."""

        self.multicast_address6 = MulticastAddress6FC(fortigate, **kwargs)
        """:py:class:`.MulticastAddress6FC` cmdb/firewall/multicast-address6."""

        self.multicast_policy = MulticastPolicyFC(fortigate, **kwargs)
        """:py:class:`.MulticastPolicyFC` cmdb/firewall/multicast-policy."""

        self.multicast_policy6 = MulticastPolicy6FC(fortigate, **kwargs)
        """:py:class:`.MulticastPolicy6FC` cmdb/firewall/multicast-policy6."""

        self.policy = PolicyFC(fortigate, **kwargs)
        """:py:class:`.PolicyFC` cmdb/firewall/policy."""

        self.policy46 = Policy46FC(fortigate, **kwargs)
        """:py:class:`.Policy46FC` cmdb/firewall/policy46."""

        self.policy64 = Policy64FC(fortigate, **kwargs)
        """:py:class:`.Policy64FC` cmdb/firewall/policy64."""

        self.profile_group = ProfileGroupFC(fortigate, **kwargs)
        """:py:class:`.ProfileGroupFC` cmdb/firewall/profile-group."""

        self.profile_protocol_options = ProfileProtocolOptionsFC(fortigate, **kwargs)
        """:py:class:`.ProfileProtocolOptionsFC` cmdb/firewall/profile-protocol-options."""

        self.proxy_address = ProxyAddressFC(fortigate, **kwargs)
        """:py:class:`.ProxyAddressFC` cmdb/firewall/proxy-address."""

        self.proxy_addrgrp = ProxyAddrgrpFC(fortigate, **kwargs)
        """:py:class:`.ProxyAddrgrpFC` cmdb/firewall/proxy-addrgrp."""

        self.proxy_policy = ProxyPolicyFC(fortigate, **kwargs)
        """:py:class:`.ProxyPolicyFC` cmdb/firewall/proxy-policy."""

        self.region = RegionFC(fortigate, **kwargs)
        """:py:class:`.RegionFC` cmdb/firewall/region."""

        self.security_policy = SecurityPolicyFC(fortigate, **kwargs)
        """:py:class:`.SecurityPolicyFC` cmdb/firewall/security-policy."""

        self.shaping_policy = ShapingPolicyFC(fortigate, **kwargs)
        """:py:class:`.ShapingPolicyFC` cmdb/firewall/shaping-policy."""

        self.shaping_profile = ShapingProfileFC(fortigate, **kwargs)
        """:py:class:`.ShapingProfileFC` cmdb/firewall/shaping-profile."""

        self.sniffer = SnifferFC(fortigate, **kwargs)
        """:py:class:`.SnifferFC` cmdb/firewall/sniffer."""

        self.ssl_server = SslServerFC(fortigate, **kwargs)
        """:py:class:`.SslServerFC` cmdb/firewall/ssl-server."""

        self.ssl_ssh_profile = SslSshProfileFC(fortigate, **kwargs)
        """:py:class:`.SslSshProfileFC` cmdb/firewall/ssl-ssh-profile."""

        self.traffic_class = TrafficClassFC(fortigate, **kwargs)
        """:py:class:`.TrafficClassFC` cmdb/firewall/traffic-class."""

        self.ttl_policy = TtlPolicyFC(fortigate, **kwargs)
        """:py:class:`.TtlPolicyFC` cmdb/firewall/ttl-policy."""

        self.vendor_mac = VendorMacFC(fortigate, **kwargs)
        """:py:class:`.VendorMacFC` cmdb/firewall/vendor-mac."""

        self.vendor_mac_summary = VendorMacSummaryFC(fortigate, **kwargs)
        """:py:class:`.VendorMacSummaryFC` cmdb/firewall/vendor-mac-summary."""

        self.vip = VipFC(fortigate, **kwargs)
        """:py:class:`.VipFC` cmdb/firewall/vip."""

        self.vip46 = Vip46FC(fortigate, **kwargs)
        """:py:class:`.Vip46FC` cmdb/firewall/vip46."""

        self.vip6 = Vip6FC(fortigate, **kwargs)
        """:py:class:`.Vip6FC` cmdb/firewall/vip6."""

        self.vip64 = Vip64FC(fortigate, **kwargs)
        """:py:class:`.Vip64FC` cmdb/firewall/vip64."""

        self.vipgrp = VipgrpFC(fortigate, **kwargs)
        """:py:class:`.VipgrpFC` cmdb/firewall/vipgrp."""

        self.vipgrp46 = Vipgrp46FC(fortigate, **kwargs)
        """:py:class:`.Vipgrp46FC` cmdb/firewall/vipgrp46."""

        self.vipgrp6 = Vipgrp6FC(fortigate, **kwargs)
        """:py:class:`.Vipgrp6FC` cmdb/firewall/vipgrp6."""

        self.vipgrp64 = Vipgrp64FC(fortigate, **kwargs)
        """:py:class:`.Vipgrp64FC` cmdb/firewall/vipgrp64."""
