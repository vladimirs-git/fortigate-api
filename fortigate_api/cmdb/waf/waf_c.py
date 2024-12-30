"""Cmdb/waf connectors."""

from fortigate_api.cmdb.waf.main_class import MainClassWC
from fortigate_api.cmdb.waf.profile import ProfileWC
from fortigate_api.cmdb.waf.signature import SignatureWC
from fortigate_api.fortigate import FortiGate


class WafC:
    """Cmdb/waf connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init WafC."""
        self.main_class = MainClassWC(fortigate, **kwargs)
        """:py:class:`.MainClassWC` cmdb/waf/main-class."""

        self.profile = ProfileWC(fortigate, **kwargs)
        """:py:class:`.ProfileWC` cmdb/waf/profile."""

        self.signature = SignatureWC(fortigate, **kwargs)
        """:py:class:`.SignatureWC` cmdb/waf/signature."""
