"""Cmdb/system/external-resource connector."""

from fortigate_api.connector import Connector


class ExternalResourceSC(Connector):
    """Cmdb/system/external-resource connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/external-resource"
    _path_ui = "ng/external-connector"
