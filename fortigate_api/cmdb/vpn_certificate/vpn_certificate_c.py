"""Cmdb/vpn.certificate connectors."""

from fortigate_api.cmdb.vpn_certificate.ca import CaVcC
from fortigate_api.cmdb.vpn_certificate.crl import CrlVcC
from fortigate_api.cmdb.vpn_certificate.local import LocalVcC
from fortigate_api.cmdb.vpn_certificate.ocsp_server import OcspServerVcC
from fortigate_api.cmdb.vpn_certificate.remote import RemoteVcC
from fortigate_api.cmdb.vpn_certificate.setting import SettingVcC
from fortigate_api.fortigate import FortiGate


class VpnCertificateC:
    """Cmdb/vpn.certificate connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init VpnCertificateC."""
        self.ca = CaVcC(fortigate, **kwargs)
        """:py:class:`.CaVcC` cmdb/vpn.certificate/ca."""

        self.crl = CrlVcC(fortigate, **kwargs)
        """:py:class:`.CrlVcC` cmdb/vpn.certificate/crl."""

        self.local = LocalVcC(fortigate, **kwargs)
        """:py:class:`.LocalVcC` cmdb/vpn.certificate/local."""

        self.ocsp_server = OcspServerVcC(fortigate, **kwargs)
        """:py:class:`.OcspServerVcC` cmdb/vpn.certificate/ocsp-server."""

        self.remote = RemoteVcC(fortigate, **kwargs)
        """:py:class:`.RemoteVcC` cmdb/vpn.certificate/remote."""

        self.setting = SettingVcC(fortigate, **kwargs)
        """:py:class:`.SettingVcC` cmdb/vpn.certificate/setting."""
