"""Cmdb/user/domain-controller connector."""

from fortigate_api.connector import Connector


class DomainControllerUC(Connector):
    """Cmdb/user/domain-controller connector."""

    uid = "name"
    _path = "api/v2/cmdb/user/domain-controller"
