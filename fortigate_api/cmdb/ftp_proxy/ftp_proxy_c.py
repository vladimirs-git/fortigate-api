"""Cmdb/ftp-proxy connectors."""

from fortigate_api.cmdb.ftp_proxy.explicit import ExplicitFpC
from fortigate_api.fortigate import FortiGate


class FtpProxyC:
    """Cmdb/ftp-proxy connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init FtpProxyC."""
        self.explicit = ExplicitFpC(fortigate, **kwargs)
        """:py:class:`.ExplicitFpC` cmdb/ftp-proxy/explicit."""
