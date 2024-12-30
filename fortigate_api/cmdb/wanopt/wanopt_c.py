"""Cmdb/wanopt connectors."""

from fortigate_api.cmdb.wanopt.auth_group import AuthGroupWC
from fortigate_api.cmdb.wanopt.cache_service import CacheServiceWC
from fortigate_api.cmdb.wanopt.content_delivery_network_rule import ContentDeliveryNetworkRuleWC
from fortigate_api.cmdb.wanopt.peer import PeerWC
from fortigate_api.cmdb.wanopt.profile import ProfileWC
from fortigate_api.cmdb.wanopt.remote_storage import RemoteStorageWC
from fortigate_api.cmdb.wanopt.settings import SettingsWC
from fortigate_api.cmdb.wanopt.webcache import WebcacheWC
from fortigate_api.fortigate import FortiGate


class WanoptC:
    """Cmdb/wanopt connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init WanoptC."""
        self.auth_group = AuthGroupWC(fortigate, **kwargs)
        """:py:class:`.AuthGroupWC` cmdb/wanopt/auth-group."""

        self.cache_service = CacheServiceWC(fortigate, **kwargs)
        """:py:class:`.CacheServiceWC` cmdb/wanopt/cache-service."""

        self.content_delivery_network_rule = ContentDeliveryNetworkRuleWC(fortigate, **kwargs)
        """:py:class:`.ContentDeliveryNetworkRuleWC` cmdb/wanopt/content-delivery-network-rule."""

        self.peer = PeerWC(fortigate, **kwargs)
        """:py:class:`.PeerWC` cmdb/wanopt/peer."""

        self.profile = ProfileWC(fortigate, **kwargs)
        """:py:class:`.ProfileWC` cmdb/wanopt/profile."""

        self.remote_storage = RemoteStorageWC(fortigate, **kwargs)
        """:py:class:`.RemoteStorageWC` cmdb/wanopt/remote-storage."""

        self.settings = SettingsWC(fortigate, **kwargs)
        """:py:class:`.SettingsWC` cmdb/wanopt/settings."""

        self.webcache = WebcacheWC(fortigate, **kwargs)
        """:py:class:`.WebcacheWC` cmdb/wanopt/webcache."""
