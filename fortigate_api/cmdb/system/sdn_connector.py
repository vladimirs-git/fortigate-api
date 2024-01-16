"""Cmdb/system/sdn-connector connector."""

from fortigate_api.connector import Connector


class SdnConnectorSC(Connector):
    """Cmdb/system/sdn-connector connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/sdn-connector"
