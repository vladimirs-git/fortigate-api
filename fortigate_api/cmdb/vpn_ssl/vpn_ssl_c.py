"""Cmdb/vpn.ssl connectors."""

from fortigate_api.cmdb.vpn_ssl.settings import SettingsVsC
from fortigate_api.fortigate import FortiGate


class VpnSslC:
    """Cmdb/vpn.ssl connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init VpnSslC."""

        self.settings = SettingsVsC(fortigate, **kwargs)
        """:py:class:`.SettingsVsC` cmdb/vpn.ssl/settings."""
