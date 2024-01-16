"""Cmdb/system.3g-modem/custom connector."""

from fortigate_api.connector import Connector


class CustomS3mC(Connector):
    """Cmdb/system.3g-modem/custom connector."""

    uid = "id"
    _path = "api/v2/cmdb/system.3g-modem/custom"
