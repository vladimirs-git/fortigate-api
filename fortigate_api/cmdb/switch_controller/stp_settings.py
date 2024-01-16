"""Cmdb/switch-controller/stp-settings connector."""

from fortigate_api.connector import Connector


class StpSettingsScC(Connector):
    """Cmdb/switch-controller/stp-settings connector."""

    uid = ""
    _path = "api/v2/cmdb/switch-controller/stp-settings"
