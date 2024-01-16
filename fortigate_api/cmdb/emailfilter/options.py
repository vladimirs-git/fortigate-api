"""Cmdb/emailfilter/options connector."""

from fortigate_api.connector import Connector


class OptionsEC(Connector):
    """Cmdb/emailfilter/options connector."""

    uid = ""
    _path = "api/v2/cmdb/emailfilter/options"
