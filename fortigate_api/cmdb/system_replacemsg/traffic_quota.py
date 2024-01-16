"""Cmdb/system.replacemsg/traffic-quota connector."""

from fortigate_api.connector import Connector


class TrafficQuotaSrC(Connector):
    """Cmdb/system.replacemsg/traffic-quota connector."""

    uid = "msg-type"
    _path = "api/v2/cmdb/system.replacemsg/traffic-quota"
