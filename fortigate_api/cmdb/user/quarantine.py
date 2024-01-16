"""Cmdb/user/quarantine connector."""

from fortigate_api.connector import Connector


class QuarantineUC(Connector):
    """Cmdb/user/quarantine connector."""

    uid = ""
    _path = "api/v2/cmdb/user/quarantine"
