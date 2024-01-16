"""Cmdb/firewall.schedule/recurring connector."""

from fortigate_api.connector import Connector


class RecurringFsC(Connector):
    """Cmdb/firewall.schedule/recurring connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall.schedule/recurring"
