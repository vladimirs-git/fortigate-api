"""Cmdb/user/password-policy connector."""

from fortigate_api.connector import Connector


class PasswordPolicyUC(Connector):
    """Cmdb/user/password-policy connector."""

    uid = "name"
    _path = "api/v2/cmdb/user/password-policy"
