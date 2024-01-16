"""Cmdb/log connectors."""

from fortigate_api.cmdb.log.custom_field import CustomFieldLC
from fortigate_api.cmdb.log.eventfilter import EventfilterLC
from fortigate_api.cmdb.log.gui_display import GuiDisplayLC
from fortigate_api.cmdb.log.setting import SettingLC
from fortigate_api.cmdb.log.threat_weight import ThreatWeightLC
from fortigate_api.fortigate import FortiGate


class LogC:
    """Cmdb/log connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init LogC."""

        self.custom_field = CustomFieldLC(fortigate, **kwargs)
        """:py:class:`.CustomFieldLC` cmdb/log/custom-field."""

        self.eventfilter = EventfilterLC(fortigate, **kwargs)
        """:py:class:`.EventfilterLC` cmdb/log/eventfilter."""

        self.gui_display = GuiDisplayLC(fortigate, **kwargs)
        """:py:class:`.GuiDisplayLC` cmdb/log/gui-display."""

        self.setting = SettingLC(fortigate, **kwargs)
        """:py:class:`.SettingLC` cmdb/log/setting."""

        self.threat_weight = ThreatWeightLC(fortigate, **kwargs)
        """:py:class:`.ThreatWeightLC` cmdb/log/threat-weight."""
