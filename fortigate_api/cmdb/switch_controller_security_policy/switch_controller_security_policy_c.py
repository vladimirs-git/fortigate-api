"""Cmdb/switch-controller.security-policy connectors."""

from fortigate_api.cmdb.switch_controller_security_policy._802_1x import _8021xScspC
from fortigate_api.fortigate import FortiGate


class SwitchControllerSecurityPolicyC:
    """Cmdb/switch-controller.security-policy connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init SwitchControllerSecurityPolicyC."""

        self._802_1x = _8021xScspC(fortigate, **kwargs)
        """:py:class:`._8021xScspC` cmdb/switch-controller.security-policy/802-1X."""
