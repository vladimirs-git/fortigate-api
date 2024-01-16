"""Cmdb/emailfilter/iptrust connector."""

from fortigate_api.connector import Connector


class IptrustEC(Connector):
    """Cmdb/emailfilter/iptrust connector."""

    uid = "id"
    _path = "api/v2/cmdb/emailfilter/iptrust"
