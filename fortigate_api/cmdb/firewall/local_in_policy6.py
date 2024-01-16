"""Cmdb/firewall/local-in-policy6 connector."""

from fortigate_api.connector import Connector


class LocalInPolicy6FC(Connector):
    """Cmdb/firewall/local-in-policy6 connector."""

    uid = "policyid"
    _path = "api/v2/cmdb/firewall/local-in-policy6"
