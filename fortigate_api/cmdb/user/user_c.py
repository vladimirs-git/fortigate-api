"""Cmdb/user connectors."""

from fortigate_api.cmdb.user.adgrp import AdgrpUC
from fortigate_api.cmdb.user.domain_controller import DomainControllerUC
from fortigate_api.cmdb.user.exchange import ExchangeUC
from fortigate_api.cmdb.user.fortitoken import FortitokenUC
from fortigate_api.cmdb.user.fsso import FssoUC
from fortigate_api.cmdb.user.fsso_polling import FssoPollingUC
from fortigate_api.cmdb.user.group import GroupUC
from fortigate_api.cmdb.user.krb_keytab import KrbKeytabUC
from fortigate_api.cmdb.user.ldap import LdapUC
from fortigate_api.cmdb.user.local import LocalUC
from fortigate_api.cmdb.user.nac_policy import NacPolicyUC
from fortigate_api.cmdb.user.password_policy import PasswordPolicyUC
from fortigate_api.cmdb.user.peer import PeerUC
from fortigate_api.cmdb.user.peergrp import PeergrpUC
from fortigate_api.cmdb.user.pop3 import Pop3UC
from fortigate_api.cmdb.user.quarantine import QuarantineUC
from fortigate_api.cmdb.user.radius import RadiusUC
from fortigate_api.cmdb.user.saml import SamlUC
from fortigate_api.cmdb.user.security_exempt_list import SecurityExemptListUC
from fortigate_api.cmdb.user.setting import SettingUC
from fortigate_api.cmdb.user.tacacs import TacacsUC
from fortigate_api.fortigate import FortiGate


class UserC:
    """Cmdb/user connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init UserC."""
        self.adgrp = AdgrpUC(fortigate, **kwargs)
        """:py:class:`.AdgrpUC` cmdb/user/adgrp."""

        self.domain_controller = DomainControllerUC(fortigate, **kwargs)
        """:py:class:`.DomainControllerUC` cmdb/user/domain-controller."""

        self.exchange = ExchangeUC(fortigate, **kwargs)
        """:py:class:`.ExchangeUC` cmdb/user/exchange."""

        self.fortitoken = FortitokenUC(fortigate, **kwargs)
        """:py:class:`.FortitokenUC` cmdb/user/fortitoken."""

        self.fsso = FssoUC(fortigate, **kwargs)
        """:py:class:`.FssoUC` cmdb/user/fsso."""

        self.fsso_polling = FssoPollingUC(fortigate, **kwargs)
        """:py:class:`.FssoPollingUC` cmdb/user/fsso-polling."""

        self.group = GroupUC(fortigate, **kwargs)
        """:py:class:`.GroupUC` cmdb/user/group."""

        self.krb_keytab = KrbKeytabUC(fortigate, **kwargs)
        """:py:class:`.KrbKeytabUC` cmdb/user/krb-keytab."""

        self.ldap = LdapUC(fortigate, **kwargs)
        """:py:class:`.LdapUC` cmdb/user/ldap."""

        self.local = LocalUC(fortigate, **kwargs)
        """:py:class:`.LocalUC` cmdb/user/local."""

        self.nac_policy = NacPolicyUC(fortigate, **kwargs)
        """:py:class:`.NacPolicyUC` cmdb/user/nac-policy."""

        self.password_policy = PasswordPolicyUC(fortigate, **kwargs)
        """:py:class:`.PasswordPolicyUC` cmdb/user/password-policy."""

        self.peer = PeerUC(fortigate, **kwargs)
        """:py:class:`.PeerUC` cmdb/user/peer."""

        self.peergrp = PeergrpUC(fortigate, **kwargs)
        """:py:class:`.PeergrpUC` cmdb/user/peergrp."""

        self.pop3 = Pop3UC(fortigate, **kwargs)
        """:py:class:`.Pop3UC` cmdb/user/pop3."""

        self.quarantine = QuarantineUC(fortigate, **kwargs)
        """:py:class:`.QuarantineUC` cmdb/user/quarantine."""

        self.radius = RadiusUC(fortigate, **kwargs)
        """:py:class:`.RadiusUC` cmdb/user/radius."""

        self.saml = SamlUC(fortigate, **kwargs)
        """:py:class:`.SamlUC` cmdb/user/saml."""

        self.security_exempt_list = SecurityExemptListUC(fortigate, **kwargs)
        """:py:class:`.SecurityExemptListUC` cmdb/user/security-exempt-list."""

        self.setting = SettingUC(fortigate, **kwargs)
        """:py:class:`.SettingUC` cmdb/user/setting."""

        self.tacacs = TacacsUC(fortigate, **kwargs)
        """:py:class:`.TacacsUC` cmdb/user/tacacs+."""
