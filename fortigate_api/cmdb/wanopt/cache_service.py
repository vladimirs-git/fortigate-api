"""Cmdb/wanopt/cache-service connector."""

from fortigate_api.connector import Connector


class CacheServiceWC(Connector):
    """Cmdb/wanopt/cache-service connector."""

    uid = ""
    _path = "api/v2/cmdb/wanopt/cache-service"
