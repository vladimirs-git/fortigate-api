"""Cmdb/system/speed-test-server connector."""

from fortigate_api.connector import Connector


class SpeedTestServerSC(Connector):
    """Cmdb/system/speed-test-server connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/speed-test-server"
