"""Cmdb/firewall.ssh/local-key connector."""

from fortigate_api.connector import Connector


class LocalKeyFsC(Connector):
    """Cmdb/firewall.ssh/local-key connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall.ssh/local-key"
