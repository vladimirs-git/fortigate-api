"""Cmdb/user/nac-policy connector."""

from fortigate_api.connector import Connector


class NacPolicyUC(Connector):
    """Cmdb/user/nac-policy connector."""

    uid = "name"
    _path = "api/v2/cmdb/user/nac-policy"
