"""Cmdb/dnsfilter/domain-filter connector."""

from fortigate_api.connector import Connector


class DomainFilterDC(Connector):
    """Cmdb/dnsfilter/domain-filter connector."""

    uid = "id"
    _path = "api/v2/cmdb/dnsfilter/domain-filter"
