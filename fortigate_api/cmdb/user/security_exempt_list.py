"""Cmdb/user/security-exempt-list connector."""

from fortigate_api.connector import Connector


class SecurityExemptListUC(Connector):
    """Cmdb/user/security-exempt-list connector."""

    uid = "name"
    _path = "api/v2/cmdb/user/security-exempt-list"
