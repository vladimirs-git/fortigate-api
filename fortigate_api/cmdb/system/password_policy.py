"""Cmdb/system/password-policy connector."""

from fortigate_api.connector import Connector


class PasswordPolicySC(Connector):
    """Cmdb/system/password-policy connector."""

    uid = ""
    _path = "api/v2/cmdb/system/password-policy"
