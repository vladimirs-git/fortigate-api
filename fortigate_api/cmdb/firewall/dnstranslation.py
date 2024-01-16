"""Cmdb/firewall/dnstranslation connector."""

from fortigate_api.connector import Connector


class DnstranslationFC(Connector):
    """Cmdb/firewall/dnstranslation connector."""

    uid = "id"
    _path = "api/v2/cmdb/firewall/dnstranslation"
