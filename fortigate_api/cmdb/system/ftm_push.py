"""Cmdb/system/ftm-push connector."""

from fortigate_api.connector import Connector


class FtmPushSC(Connector):
    """Cmdb/system/ftm-push connector."""

    uid = ""
    _path = "api/v2/cmdb/system/ftm-push"
