"""Cmdb/certificate/remote connector."""

from fortigate_api.connector import Connector


class RemoteCC(Connector):
    """Cmdb/certificate/remote connector."""

    uid = "name"
    _path = "api/v2/cmdb/certificate/remote"
