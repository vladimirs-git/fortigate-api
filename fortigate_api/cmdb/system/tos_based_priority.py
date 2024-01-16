"""Cmdb/system/tos-based-priority connector."""

from fortigate_api.connector import Connector


class TosBasedPrioritySC(Connector):
    """Cmdb/system/tos-based-priority connector."""

    uid = "id"
    _path = "api/v2/cmdb/system/tos-based-priority"
