"""Cmdb/system.3g-modem connectors."""

from fortigate_api.cmdb.system_3g_modem.custom import CustomS3mC
from fortigate_api.fortigate import FortiGate


class System3gModemC:
    """Cmdb/system.3g-modem connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init System3gModemC."""

        self.custom = CustomS3mC(fortigate, **kwargs)
        """:py:class:`.CustomS3mC` cmdb/system.3g-modem/custom."""
