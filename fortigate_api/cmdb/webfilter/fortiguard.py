"""Cmdb/webfilter/fortiguard connector."""

from fortigate_api.connector import Connector


class FortiguardWC(Connector):
    """Cmdb/webfilter/fortiguard connector."""

    uid = ""
    _path = "api/v2/cmdb/webfilter/fortiguard"
