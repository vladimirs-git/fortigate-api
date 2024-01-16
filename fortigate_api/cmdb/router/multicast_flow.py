"""Cmdb/router/multicast-flow connector."""

from fortigate_api.connector import Connector


class MulticastFlowRC(Connector):
    """Cmdb/router/multicast-flow connector."""

    uid = "name"
    _path = "api/v2/cmdb/router/multicast-flow"
