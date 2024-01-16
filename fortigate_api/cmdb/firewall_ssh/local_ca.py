"""Cmdb/firewall.ssh/local-ca connector."""

from fortigate_api.connector import Connector


class LocalCaFsC(Connector):
    """Cmdb/firewall.ssh/local-ca connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall.ssh/local-ca"
