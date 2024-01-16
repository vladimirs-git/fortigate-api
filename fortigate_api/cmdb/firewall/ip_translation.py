"""Cmdb/firewall/ip-translation connector."""

from fortigate_api.connector import Connector


class IpTranslationFC(Connector):
    """Cmdb/firewall/ip-translation connector."""

    uid = "transid"
    _path = "api/v2/cmdb/firewall/ip-translation"
