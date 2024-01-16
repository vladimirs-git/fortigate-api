"""Cmdb/system/accprofile connector."""

from fortigate_api.connector import Connector


class AccprofileSC(Connector):
    """Cmdb/system/accprofile connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/accprofile"
