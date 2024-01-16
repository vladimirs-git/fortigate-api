"""Cmdb/ips/decoder connector."""

from fortigate_api.connector import Connector


class DecoderIC(Connector):
    """Cmdb/ips/decoder connector."""

    uid = "name"
    _path = "api/v2/cmdb/ips/decoder"
