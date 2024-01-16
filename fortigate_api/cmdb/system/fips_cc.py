"""Cmdb/system/fips-cc connector."""

from fortigate_api.connector import Connector


class FipsCcSC(Connector):
    """Cmdb/system/fips-cc connector."""

    uid = ""
    _path = "api/v2/cmdb/system/fips-cc"
