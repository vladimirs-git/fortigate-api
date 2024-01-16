"""Cmdb/vpn connectors."""

from fortigate_api.cmdb.vpn.l2tp import L2tpVC
from fortigate_api.cmdb.vpn.ocvpn import OcvpnVC
from fortigate_api.cmdb.vpn.pptp import PptpVC
from fortigate_api.fortigate import FortiGate


class VpnC:
    """Cmdb/vpn connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init VpnC."""

        self.l2tp = L2tpVC(fortigate, **kwargs)
        """:py:class:`.L2tpVC` cmdb/vpn/l2tp."""

        self.ocvpn = OcvpnVC(fortigate, **kwargs)
        """:py:class:`.OcvpnVC` cmdb/vpn/ocvpn."""

        self.pptp = PptpVC(fortigate, **kwargs)
        """:py:class:`.PptpVC` cmdb/vpn/pptp."""
