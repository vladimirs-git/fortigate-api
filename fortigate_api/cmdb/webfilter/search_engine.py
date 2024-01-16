"""Cmdb/webfilter/search-engine connector."""

from fortigate_api.connector import Connector


class SearchEngineWC(Connector):
    """Cmdb/webfilter/search-engine connector."""

    uid = "name"
    _path = "api/v2/cmdb/webfilter/search-engine"
