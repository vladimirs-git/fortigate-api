"""Cmdb/vpn.ssl.web connectors."""

from fortigate_api.cmdb.vpn_ssl_web.host_check_software import HostCheckSoftwareVswC
from fortigate_api.cmdb.vpn_ssl_web.portal import PortalVswC
from fortigate_api.cmdb.vpn_ssl_web.realm import RealmVswC
from fortigate_api.cmdb.vpn_ssl_web.user_bookmark import UserBookmarkVswC
from fortigate_api.cmdb.vpn_ssl_web.user_group_bookmark import UserGroupBookmarkVswC
from fortigate_api.fortigate import FortiGate


class VpnSslWebC:
    """Cmdb/vpn.ssl.web connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init VpnSslWebC."""
        self.host_check_software = HostCheckSoftwareVswC(fortigate, **kwargs)
        """:py:class:`.HostCheckSoftwareVswC` cmdb/vpn.ssl.web/host-check-software."""

        self.portal = PortalVswC(fortigate, **kwargs)
        """:py:class:`.PortalVswC` cmdb/vpn.ssl.web/portal."""

        self.realm = RealmVswC(fortigate, **kwargs)
        """:py:class:`.RealmVswC` cmdb/vpn.ssl.web/realm."""

        self.user_bookmark = UserBookmarkVswC(fortigate, **kwargs)
        """:py:class:`.UserBookmarkVswC` cmdb/vpn.ssl.web/user-bookmark."""

        self.user_group_bookmark = UserGroupBookmarkVswC(fortigate, **kwargs)
        """:py:class:`.UserGroupBookmarkVswC` cmdb/vpn.ssl.web/user-group-bookmark."""
