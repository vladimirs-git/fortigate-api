"""Cmdb/system/fortisandbox connector."""

from fortigate_api.connector import Connector


class FortisandboxSC(Connector):
    """Cmdb/system/fortisandbox connector."""

    uid = ""
    _path = "api/v2/cmdb/system/fortisandbox"
