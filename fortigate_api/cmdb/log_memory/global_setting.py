"""Cmdb/log.memory/global-setting connector."""

from fortigate_api.connector import Connector


class GlobalSettingLmC(Connector):
    """Cmdb/log.memory/global-setting connector."""

    uid = ""
    _path = "api/v2/cmdb/log.memory/global-setting"
