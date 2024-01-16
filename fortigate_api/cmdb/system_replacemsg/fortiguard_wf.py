"""Cmdb/system.replacemsg/fortiguard-wf connector."""

from fortigate_api.connector import Connector


class FortiguardWfSrC(Connector):
    """Cmdb/system.replacemsg/fortiguard-wf connector."""

    uid = "msg-type"
    _path = "api/v2/cmdb/system.replacemsg/fortiguard-wf"
