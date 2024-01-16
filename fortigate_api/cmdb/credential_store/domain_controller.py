"""Cmdb/credential-store/domain-controller connector."""

from fortigate_api.connector import Connector


class DomainControllerCsC(Connector):
    """Cmdb/credential-store/domain-controller connector."""

    uid = "server-name"
    _path = "api/v2/cmdb/credential-store/domain-controller"
