"""Cmdb/system.replacemsg/icap connector."""

from fortigate_api.connector import Connector


class IcapSrC(Connector):
    """Cmdb/system.replacemsg/icap connector."""

    uid = "msg-type"
    _path = "api/v2/cmdb/system.replacemsg/icap"
