"""Cmdb/system.autoupdate/schedule connector."""

from fortigate_api.connector import Connector


class ScheduleSaC(Connector):
    """Cmdb/system.autoupdate/schedule connector."""

    uid = ""
    _path = "api/v2/cmdb/system.autoupdate/schedule"
