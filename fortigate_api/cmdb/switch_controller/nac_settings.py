"""Cmdb/switch-controller/nac-settings connector."""

from fortigate_api.connector import Connector


class NacSettingsScC(Connector):
    """Cmdb/switch-controller/nac-settings connector."""

    uid = "name"
    _path = "api/v2/cmdb/switch-controller/nac-settings"
