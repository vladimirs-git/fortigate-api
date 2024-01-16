"""Cmdb/user/fortitoken connector."""

from fortigate_api.connector import Connector


class FortitokenUC(Connector):
    """Cmdb/user/fortitoken connector."""

    uid = "serial-number"
    _path = "api/v2/cmdb/user/fortitoken"
