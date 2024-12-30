"""Cmdb/ips connectors."""

from fortigate_api.cmdb.ips.custom import CustomIC
from fortigate_api.cmdb.ips.decoder import DecoderIC
from fortigate_api.cmdb.ips.global_ import GlobalIC
from fortigate_api.cmdb.ips.rule import RuleIC
from fortigate_api.cmdb.ips.rule_settings import RuleSettingsIC
from fortigate_api.cmdb.ips.sensor import SensorIC
from fortigate_api.cmdb.ips.settings import SettingsIC
from fortigate_api.cmdb.ips.view_map import ViewMapIC
from fortigate_api.fortigate import FortiGate


class IpsC:
    """Cmdb/ips connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init IpsC."""
        self.custom = CustomIC(fortigate, **kwargs)
        """:py:class:`.CustomIC` cmdb/ips/custom."""

        self.decoder = DecoderIC(fortigate, **kwargs)
        """:py:class:`.DecoderIC` cmdb/ips/decoder."""

        self.global_ = GlobalIC(fortigate, **kwargs)
        """:py:class:`.GlobalIC` cmdb/ips/global."""

        self.rule = RuleIC(fortigate, **kwargs)
        """:py:class:`.RuleIC` cmdb/ips/rule."""

        self.rule_settings = RuleSettingsIC(fortigate, **kwargs)
        """:py:class:`.RuleSettingsIC` cmdb/ips/rule-settings."""

        self.sensor = SensorIC(fortigate, **kwargs)
        """:py:class:`.SensorIC` cmdb/ips/sensor."""

        self.settings = SettingsIC(fortigate, **kwargs)
        """:py:class:`.SettingsIC` cmdb/ips/settings."""

        self.view_map = ViewMapIC(fortigate, **kwargs)
        """:py:class:`.ViewMapIC` cmdb/ips/view-map."""
