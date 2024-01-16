"""Cmdb/system/cluster-sync connector."""

from fortigate_api.connector import Connector


class ClusterSyncSC(Connector):
    """Cmdb/system/cluster-sync connector."""

    uid = "sync-id"
    _path = "api/v2/cmdb/system/cluster-sync"
