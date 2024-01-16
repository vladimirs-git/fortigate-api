"""Cmdb/system/automation-action connector."""

from fortigate_api.connector import Connector


class AutomationActionSC(Connector):
    """Cmdb/system/automation-action connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/automation-action"
