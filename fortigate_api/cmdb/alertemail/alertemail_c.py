"""Cmdb/alertemail connectors."""

from fortigate_api.cmdb.alertemail.setting import SettingAC
from fortigate_api.fortigate import FortiGate


class AlertemailC:
    """Cmdb/alertemail connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init AlertemailC."""

        self.setting = SettingAC(fortigate, **kwargs)
        """:py:class:`.SettingAC` cmdb/alertemail/setting."""
