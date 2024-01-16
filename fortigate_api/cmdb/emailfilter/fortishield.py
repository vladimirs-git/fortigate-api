"""Cmdb/emailfilter/fortishield connector."""

from fortigate_api.connector import Connector


class FortishieldEC(Connector):
    """Cmdb/emailfilter/fortishield connector."""

    uid = ""
    _path = "api/v2/cmdb/emailfilter/fortishield"
