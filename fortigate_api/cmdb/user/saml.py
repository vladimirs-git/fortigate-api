"""Cmdb/user/saml connector."""

from fortigate_api.connector import Connector


class SamlUC(Connector):
    """Cmdb/user/saml connector."""

    uid = "name"
    _path = "api/v2/cmdb/user/saml"
