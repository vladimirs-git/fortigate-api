"""Cmdb/system/resource-limits connector."""

from fortigate_api.connector import Connector


class ResourceLimitsSC(Connector):
    """Cmdb/system/resource-limits connector."""

    uid = ""
    _path = "api/v2/cmdb/system/resource-limits"
