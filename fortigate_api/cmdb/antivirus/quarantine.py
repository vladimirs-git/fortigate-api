"""Cmdb/antivirus/quarantine connector."""

from fortigate_api.connector import Connector


class QuarantineAC(Connector):
    """Cmdb/antivirus/quarantine connector."""

    uid = ""
    _path = "api/v2/cmdb/antivirus/quarantine"
