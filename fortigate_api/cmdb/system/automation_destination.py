"""Cmdb/system/automation-destination connector."""

from fortigate_api.connector import Connector


class AutomationDestinationSC(Connector):
    """Cmdb/system/automation-destination connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/automation-destination"
