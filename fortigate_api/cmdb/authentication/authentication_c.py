"""Cmdb/authentication connectors."""

from fortigate_api.cmdb.authentication.rule import RuleAC
from fortigate_api.cmdb.authentication.scheme import SchemeAC
from fortigate_api.cmdb.authentication.setting import SettingAC
from fortigate_api.fortigate import FortiGate


class AuthenticationC:
    """Cmdb/authentication connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init AuthenticationC."""
        self.rule = RuleAC(fortigate, **kwargs)
        """:py:class:`.RuleAC` cmdb/authentication/rule."""

        self.scheme = SchemeAC(fortigate, **kwargs)
        """:py:class:`.SchemeAC` cmdb/authentication/scheme."""

        self.setting = SettingAC(fortigate, **kwargs)
        """:py:class:`.SettingAC` cmdb/authentication/setting."""
