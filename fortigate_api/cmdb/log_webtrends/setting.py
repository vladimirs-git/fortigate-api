"""Cmdb/log.webtrends/setting connector."""

from fortigate_api.connector import Connector


class SettingLwC(Connector):
    """Cmdb/log.webtrends/setting connector."""

    uid = ""
    _path = "api/v2/cmdb/log.webtrends/setting"
