"""Cmdb/system/saml connector."""

from fortigate_api.connector import Connector


class SamlSC(Connector):
    """Cmdb/system/saml connector."""

    uid = ""
    _path = "api/v2/cmdb/system/saml"
