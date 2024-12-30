"""Cmdb/dlp connectors."""

from fortigate_api.cmdb.dlp.filepattern import FilepatternDC
from fortigate_api.cmdb.dlp.fp_doc_source import FpDocSourceDC
from fortigate_api.cmdb.dlp.sensitivity import SensitivityDC
from fortigate_api.cmdb.dlp.sensor import SensorDC
from fortigate_api.cmdb.dlp.settings import SettingsDC
from fortigate_api.fortigate import FortiGate


class DlpC:
    """Cmdb/dlp connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init DlpC."""
        self.filepattern = FilepatternDC(fortigate, **kwargs)
        """:py:class:`.FilepatternDC` cmdb/dlp/filepattern."""

        self.fp_doc_source = FpDocSourceDC(fortigate, **kwargs)
        """:py:class:`.FpDocSourceDC` cmdb/dlp/fp-doc-source."""

        self.sensitivity = SensitivityDC(fortigate, **kwargs)
        """:py:class:`.SensitivityDC` cmdb/dlp/sensitivity."""

        self.sensor = SensorDC(fortigate, **kwargs)
        """:py:class:`.SensorDC` cmdb/dlp/sensor."""

        self.settings = SettingsDC(fortigate, **kwargs)
        """:py:class:`.SettingsDC` cmdb/dlp/settings."""
