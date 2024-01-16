"""Cmdb/system/replacemsg-image connector."""

from fortigate_api.connector import Connector


class ReplacemsgImageSC(Connector):
    """Cmdb/system/replacemsg-image connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/replacemsg-image"
