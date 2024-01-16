"""Cmdb/application/rule-settings connector."""

from fortigate_api.connector import Connector


class RuleSettingsAC(Connector):
    """Cmdb/application/rule-settings connector."""

    uid = "id"
    _path = "api/v2/cmdb/application/rule-settings"
