"""Cmdb/extender-controller connectors."""

from fortigate_api.cmdb.extender_controller.dataplan import DataplanEcC
from fortigate_api.cmdb.extender_controller.extender import ExtenderEcC
from fortigate_api.fortigate import FortiGate


class ExtenderControllerC:
    """Cmdb/extender-controller connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init ExtenderControllerC."""

        self.dataplan = DataplanEcC(fortigate, **kwargs)
        """:py:class:`.DataplanEcC` cmdb/extender-controller/dataplan."""

        self.extender = ExtenderEcC(fortigate, **kwargs)
        """:py:class:`.ExtenderEcC` cmdb/extender-controller/extender."""
