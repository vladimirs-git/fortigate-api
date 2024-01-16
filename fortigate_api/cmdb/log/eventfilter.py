"""Cmdb/log/eventfilter connector."""

from fortigate_api.connector import Connector


class EventfilterLC(Connector):
    """Cmdb/log/eventfilter connector."""

    uid = ""
    _path = "api/v2/cmdb/log/eventfilter"
