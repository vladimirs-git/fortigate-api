"""Cmdb/emailfilter/mheader connector."""

from fortigate_api.connector import Connector


class MheaderEC(Connector):
    """Cmdb/emailfilter/mheader connector."""

    uid = "id"
    _path = "api/v2/cmdb/emailfilter/mheader"
