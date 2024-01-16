"""Cmdb/system/password-policy-guest-admin connector."""

from fortigate_api.connector import Connector


class PasswordPolicyGuestAdminSC(Connector):
    """Cmdb/system/password-policy-guest-admin connector."""

    uid = ""
    _path = "api/v2/cmdb/system/password-policy-guest-admin"
