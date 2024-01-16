"""Cmdb/wanopt/content-delivery-network-rule connector."""

from fortigate_api.connector import Connector


class ContentDeliveryNetworkRuleWC(Connector):
    """Cmdb/wanopt/content-delivery-network-rule connector."""

    uid = "name"
    _path = "api/v2/cmdb/wanopt/content-delivery-network-rule"
