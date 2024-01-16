"""Cmdb/router/policy connector."""

from fortigate_api.connector import Connector


class PolicyRC(Connector):
    """Cmdb/router/policy connector."""

    uid = "seq-num"
    _path = "api/v2/cmdb/router/policy"
