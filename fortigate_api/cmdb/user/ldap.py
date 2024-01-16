"""Cmdb/user/ldap connector."""

from fortigate_api.connector import Connector


class LdapUC(Connector):
    """Cmdb/user/ldap connector."""

    uid = "name"
    _path = "api/v2/cmdb/user/ldap"
