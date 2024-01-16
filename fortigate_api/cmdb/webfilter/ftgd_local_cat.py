"""Cmdb/webfilter/ftgd-local-cat connector."""

from fortigate_api.connector import Connector


class FtgdLocalCatWC(Connector):
    """Cmdb/webfilter/ftgd-local-cat connector."""

    uid = "desc"
    _path = "api/v2/cmdb/webfilter/ftgd-local-cat"
