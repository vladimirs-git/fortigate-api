"""Cmdb/emailfilter/dnsbl connector."""

from fortigate_api.connector import Connector


class DnsblEC(Connector):
    """Cmdb/emailfilter/dnsbl connector."""

    uid = "id"
    _path = "api/v2/cmdb/emailfilter/dnsbl"
