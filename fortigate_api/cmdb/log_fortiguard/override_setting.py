"""Cmdb/log.fortiguard/override-setting connector."""

from fortigate_api.connector import Connector


class OverrideSettingLfC(Connector):
    """Cmdb/log.fortiguard/override-setting connector."""

    uid = ""
    _path = "api/v2/cmdb/log.fortiguard/override-setting"
