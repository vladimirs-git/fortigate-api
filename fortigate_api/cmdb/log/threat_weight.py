"""Cmdb/log/threat-weight connector."""

from fortigate_api.connector import Connector


class ThreatWeightLC(Connector):
    """Cmdb/log/threat-weight connector."""

    uid = ""
    _path = "api/v2/cmdb/log/threat-weight"
