"""Cmdb/waf/signature connector."""

from fortigate_api.connector import Connector


class SignatureWC(Connector):
    """Cmdb/waf/signature connector."""

    uid = "id"
    _path = "api/v2/cmdb/waf/signature"
