"""Cmdb/firewall.wildcard-fqdn/group connector."""

from fortigate_api.connector import Connector


class GroupFwfC(Connector):
    """Cmdb/firewall.wildcard-fqdn/group connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall.wildcard-fqdn/group"
