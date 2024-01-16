"""Cmdb/system/standalone-cluster connector."""

from fortigate_api.connector import Connector


class StandaloneClusterSC(Connector):
    """Cmdb/system/standalone-cluster connector."""

    uid = ""
    _path = "api/v2/cmdb/system/standalone-cluster"
