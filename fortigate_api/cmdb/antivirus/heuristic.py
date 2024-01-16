"""Cmdb/antivirus/heuristic connector."""

from fortigate_api.connector import Connector


class HeuristicAC(Connector):
    """Cmdb/antivirus/heuristic connector."""

    uid = ""
    _path = "api/v2/cmdb/antivirus/heuristic"
