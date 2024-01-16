"""Cmdb/firewall/acl connector."""

from fortigate_api.connector import Connector


class AclFC(Connector):
    """Cmdb/firewall/acl connector."""

    uid = "policyid"
    _path = "api/v2/cmdb/firewall/acl"
