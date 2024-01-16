"""Cmdb/antivirus connectors."""

from fortigate_api.cmdb.antivirus.heuristic import HeuristicAC
from fortigate_api.cmdb.antivirus.profile import ProfileAC
from fortigate_api.cmdb.antivirus.quarantine import QuarantineAC
from fortigate_api.cmdb.antivirus.settings import SettingsAC
from fortigate_api.fortigate import FortiGate


class AntivirusC:
    """Cmdb/antivirus connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init AntivirusC."""

        self.heuristic = HeuristicAC(fortigate, **kwargs)
        """:py:class:`.HeuristicAC` cmdb/antivirus/heuristic."""

        self.profile = ProfileAC(fortigate, **kwargs)
        """:py:class:`.ProfileAC` cmdb/antivirus/profile."""

        self.quarantine = QuarantineAC(fortigate, **kwargs)
        """:py:class:`.QuarantineAC` cmdb/antivirus/quarantine."""

        self.settings = SettingsAC(fortigate, **kwargs)
        """:py:class:`.SettingsAC` cmdb/antivirus/settings."""
