"""Cmdb/system/dscp-based-priority connector."""

from fortigate_api.connector import Connector


class DscpBasedPrioritySC(Connector):
    """Cmdb/system/dscp-based-priority connector."""

    uid = "id"
    _path = "api/v2/cmdb/system/dscp-based-priority"
