"""Cmdb/voip connectors."""

from fortigate_api.cmdb.voip.profile import ProfileVC
from fortigate_api.fortigate import FortiGate


class VoipC:
    """Cmdb/voip connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init VoipC."""

        self.profile = ProfileVC(fortigate, **kwargs)
        """:py:class:`.ProfileVC` cmdb/voip/profile."""
