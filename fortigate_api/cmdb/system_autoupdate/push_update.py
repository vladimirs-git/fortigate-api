"""Cmdb/system.autoupdate/push-update connector."""

from fortigate_api.connector import Connector


class PushUpdateSaC(Connector):
    """Cmdb/system.autoupdate/push-update connector."""

    uid = ""
    _path = "api/v2/cmdb/system.autoupdate/push-update"
