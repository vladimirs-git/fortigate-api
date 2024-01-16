"""Cmdb/certificate/local connector."""

from fortigate_api.connector import Connector


class LocalCC(Connector):
    """Cmdb/certificate/local connector."""

    uid = "name"
    _path = "api/v2/cmdb/certificate/local"
