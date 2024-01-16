"""Cmdb/firewall.wildcard-fqdn/custom connector."""

from fortigate_api.connector import Connector


class CustomFwfC(Connector):
    """Cmdb/firewall.wildcard-fqdn/custom connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall.wildcard-fqdn/custom"
