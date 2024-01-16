"""Cmdb/system.replacemsg/nac-quar connector."""

from fortigate_api.connector import Connector


class NacQuarSrC(Connector):
    """Cmdb/system.replacemsg/nac-quar connector."""

    uid = "msg-type"
    _path = "api/v2/cmdb/system.replacemsg/nac-quar"
