"""Cmdb/switch-controller/stp-instance connector."""

from fortigate_api.connector import Connector


class StpInstanceScC(Connector):
    """Cmdb/switch-controller/stp-instance connector."""

    uid = "id"
    _path = "api/v2/cmdb/switch-controller/stp-instance"
