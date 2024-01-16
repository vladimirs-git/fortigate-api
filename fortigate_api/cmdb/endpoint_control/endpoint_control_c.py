"""Cmdb/endpoint-control connectors."""

from fortigate_api.cmdb.endpoint_control.fctems import FctemsEcC
from fortigate_api.fortigate import FortiGate


class EndpointControlC:
    """Cmdb/endpoint-control connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init EndpointControlC."""

        self.fctems = FctemsEcC(fortigate, **kwargs)
        """:py:class:`.FctemsEcC` cmdb/endpoint-control/fctems."""
