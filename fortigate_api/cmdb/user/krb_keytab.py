"""Cmdb/user/krb-keytab connector."""

from fortigate_api.connector import Connector


class KrbKeytabUC(Connector):
    """Cmdb/user/krb-keytab connector."""

    uid = "name"
    _path = "api/v2/cmdb/user/krb-keytab"
