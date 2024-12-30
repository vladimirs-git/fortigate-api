"""Cmdb/application connectors."""

from fortigate_api.cmdb.application.custom import CustomAC
from fortigate_api.cmdb.application.group import GroupAC
from fortigate_api.cmdb.application.list import ListAC
from fortigate_api.cmdb.application.name import NameAC
from fortigate_api.cmdb.application.rule_settings import RuleSettingsAC
from fortigate_api.fortigate import FortiGate


class ApplicationC:
    """Cmdb/application connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init ApplicationC."""
        self.custom = CustomAC(fortigate, **kwargs)
        """:py:class:`.CustomAC` cmdb/application/custom."""

        self.group = GroupAC(fortigate, **kwargs)
        """:py:class:`.GroupAC` cmdb/application/group."""

        self.list = ListAC(fortigate, **kwargs)
        """:py:class:`.ListAC` cmdb/application/list."""

        self.name = NameAC(fortigate, **kwargs)
        """:py:class:`.NameAC` cmdb/application/name."""

        self.rule_settings = RuleSettingsAC(fortigate, **kwargs)
        """:py:class:`.RuleSettingsAC` cmdb/application/rule-settings."""
