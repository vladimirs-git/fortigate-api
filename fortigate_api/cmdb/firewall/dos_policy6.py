"""Cmdb/firewall/dos-policy6 connector."""

from fortigate_api.connector import Connector


class DosPolicy6FC(Connector):
    """Cmdb/firewall/dos-policy6 connector."""

    uid = "policyid"
    _path = "api/v2/cmdb/firewall/DoS-policy6"
