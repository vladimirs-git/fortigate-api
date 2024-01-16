"""Cmdb/system/automation-stitch connector."""

from fortigate_api.connector import Connector


class AutomationStitchSC(Connector):
    """Cmdb/system/automation-stitch connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/automation-stitch"
