"""Cmdb/user/exchange connector."""

from fortigate_api.connector import Connector


class ExchangeUC(Connector):
    """Cmdb/user/exchange connector."""

    uid = "name"
    _path = "api/v2/cmdb/user/exchange"
