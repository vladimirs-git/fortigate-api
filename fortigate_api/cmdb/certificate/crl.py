"""Cmdb/certificate/crl connector."""

from fortigate_api.connector import Connector


class CrlCC(Connector):
    """Cmdb/certificate/crl connector."""

    uid = "name"
    _path = "api/v2/cmdb/certificate/crl"
