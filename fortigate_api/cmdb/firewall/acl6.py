"""Cmdb/firewall/acl6 connector."""

from fortigate_api.connector import Connector


class Acl6FC(Connector):
    """Cmdb/firewall/acl6 connector."""

    uid = "policyid"
    _path = "api/v2/cmdb/firewall/acl6"
