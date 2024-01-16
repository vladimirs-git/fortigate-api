"""Cmdb/system/fortiguard connector."""

from fortigate_api.connector import Connector


class FortiguardSC(Connector):
    """Cmdb/system/fortiguard connector."""

    uid = ""
    _path = "api/v2/cmdb/system/fortiguard"
