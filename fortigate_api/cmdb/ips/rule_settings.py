"""Cmdb/ips/rule-settings connector."""

from fortigate_api.connector import Connector


class RuleSettingsIC(Connector):
    """Cmdb/ips/rule-settings connector."""

    uid = "id"
    _path = "api/v2/cmdb/ips/rule-settings"
