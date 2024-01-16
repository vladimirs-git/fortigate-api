"""Cmdb/web-proxy connectors."""

from fortigate_api.cmdb.web_proxy.debug_url import DebugUrlWpC
from fortigate_api.cmdb.web_proxy.explicit import ExplicitWpC
from fortigate_api.cmdb.web_proxy.forward_server import ForwardServerWpC
from fortigate_api.cmdb.web_proxy.forward_server_group import ForwardServerGroupWpC
from fortigate_api.cmdb.web_proxy.global_ import GlobalWpC
from fortigate_api.cmdb.web_proxy.profile import ProfileWpC
from fortigate_api.cmdb.web_proxy.url_match import UrlMatchWpC
from fortigate_api.cmdb.web_proxy.wisp import WispWpC
from fortigate_api.fortigate import FortiGate


class WebProxyC:
    """Cmdb/web-proxy connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init WebProxyC."""

        self.debug_url = DebugUrlWpC(fortigate, **kwargs)
        """:py:class:`.DebugUrlWpC` cmdb/web-proxy/debug-url."""

        self.explicit = ExplicitWpC(fortigate, **kwargs)
        """:py:class:`.ExplicitWpC` cmdb/web-proxy/explicit."""

        self.forward_server = ForwardServerWpC(fortigate, **kwargs)
        """:py:class:`.ForwardServerWpC` cmdb/web-proxy/forward-server."""

        self.forward_server_group = ForwardServerGroupWpC(fortigate, **kwargs)
        """:py:class:`.ForwardServerGroupWpC` cmdb/web-proxy/forward-server-group."""

        self.global_ = GlobalWpC(fortigate, **kwargs)
        """:py:class:`.GlobalWpC` cmdb/web-proxy/global."""

        self.profile = ProfileWpC(fortigate, **kwargs)
        """:py:class:`.ProfileWpC` cmdb/web-proxy/profile."""

        self.url_match = UrlMatchWpC(fortigate, **kwargs)
        """:py:class:`.UrlMatchWpC` cmdb/web-proxy/url-match."""

        self.wisp = WispWpC(fortigate, **kwargs)
        """:py:class:`.WispWpC` cmdb/web-proxy/wisp."""
