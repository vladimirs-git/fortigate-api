"""Cmdb/user/radius connector."""

from fortigate_api.connector import Connector


class RadiusUC(Connector):
    """Cmdb/user/radius connector."""

    uid = "name"
    _path = "api/v2/cmdb/user/radius"
