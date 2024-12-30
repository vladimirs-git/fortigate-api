"""Cmdb/vpn.ipsec connectors."""

from fortigate_api.cmdb.vpn_ipsec.concentrator import ConcentratorViC
from fortigate_api.cmdb.vpn_ipsec.forticlient import ForticlientViC
from fortigate_api.cmdb.vpn_ipsec.manualkey import ManualkeyViC
from fortigate_api.cmdb.vpn_ipsec.manualkey_interface import ManualkeyInterfaceViC
from fortigate_api.cmdb.vpn_ipsec.phase1 import Phase1ViC
from fortigate_api.cmdb.vpn_ipsec.phase1_interface import Phase1InterfaceViC
from fortigate_api.cmdb.vpn_ipsec.phase2 import Phase2ViC
from fortigate_api.cmdb.vpn_ipsec.phase2_interface import Phase2InterfaceViC
from fortigate_api.fortigate import FortiGate


class VpnIpsecC:
    """Cmdb/vpn.ipsec connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init VpnIpsecC."""
        self.concentrator = ConcentratorViC(fortigate, **kwargs)
        """:py:class:`.ConcentratorViC` cmdb/vpn.ipsec/concentrator."""

        self.forticlient = ForticlientViC(fortigate, **kwargs)
        """:py:class:`.ForticlientViC` cmdb/vpn.ipsec/forticlient."""

        self.manualkey = ManualkeyViC(fortigate, **kwargs)
        """:py:class:`.ManualkeyViC` cmdb/vpn.ipsec/manualkey."""

        self.manualkey_interface = ManualkeyInterfaceViC(fortigate, **kwargs)
        """:py:class:`.ManualkeyInterfaceViC` cmdb/vpn.ipsec/manualkey-interface."""

        self.phase1 = Phase1ViC(fortigate, **kwargs)
        """:py:class:`.Phase1ViC` cmdb/vpn.ipsec/phase1."""

        self.phase1_interface = Phase1InterfaceViC(fortigate, **kwargs)
        """:py:class:`.Phase1InterfaceViC` cmdb/vpn.ipsec/phase1-interface."""

        self.phase2 = Phase2ViC(fortigate, **kwargs)
        """:py:class:`.Phase2ViC` cmdb/vpn.ipsec/phase2."""

        self.phase2_interface = Phase2InterfaceViC(fortigate, **kwargs)
        """:py:class:`.Phase2InterfaceViC` cmdb/vpn.ipsec/phase2-interface."""
