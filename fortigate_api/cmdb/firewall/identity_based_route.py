"""Cmdb/firewall/identity-based-route connector."""

from fortigate_api.connector import Connector


class IdentityBasedRouteFC(Connector):
    """Cmdb/firewall/identity-based-route connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/identity-based-route"
