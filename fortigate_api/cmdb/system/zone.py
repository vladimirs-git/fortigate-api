"""Cmdb/system/zone connector."""

from fortigate_api.connector import Connector


class ZoneSC(Connector):
    """Cmdb/system/zone connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/zone"
    _path_ui = "ng/interface"
