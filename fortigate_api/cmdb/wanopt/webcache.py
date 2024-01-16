"""Cmdb/wanopt/webcache connector."""

from fortigate_api.connector import Connector


class WebcacheWC(Connector):
    """Cmdb/wanopt/webcache connector."""

    uid = ""
    _path = "api/v2/cmdb/wanopt/webcache"
