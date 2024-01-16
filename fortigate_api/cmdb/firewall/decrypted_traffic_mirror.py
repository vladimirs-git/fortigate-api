"""Cmdb/firewall/decrypted-traffic-mirror connector."""

from fortigate_api.connector import Connector


class DecryptedTrafficMirrorFC(Connector):
    """Cmdb/firewall/decrypted-traffic-mirror connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/decrypted-traffic-mirror"
