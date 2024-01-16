"""Cmdb/switch-controller/mac-policy connector."""

from fortigate_api.connector import Connector


class MacPolicyScC(Connector):
    """Cmdb/switch-controller/mac-policy connector."""

    uid = "name"
    _path = "api/v2/cmdb/switch-controller/mac-policy"
