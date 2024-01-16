"""Cmdb/certificate/ca connector."""

from fortigate_api.connector import Connector


class CaCC(Connector):
    """Cmdb/certificate/ca connector."""

    uid = "name"
    _path = "api/v2/cmdb/certificate/ca"
