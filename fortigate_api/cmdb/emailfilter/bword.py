"""Cmdb/emailfilter/bword connector."""

from fortigate_api.connector import Connector


class BwordEC(Connector):
    """Cmdb/emailfilter/bword connector."""

    uid = "id"
    _path = "api/v2/cmdb/emailfilter/bword"
