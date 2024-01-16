"""Cmdb/system/automation-trigger connector."""

from fortigate_api.connector import Connector


class AutomationTriggerSC(Connector):
    """Cmdb/system/automation-trigger connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/automation-trigger"
