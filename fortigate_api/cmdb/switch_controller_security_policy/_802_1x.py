"""Cmdb/switch-controller.security-policy/802-1x connector."""

from fortigate_api.connector import Connector


class _8021xScspC(Connector):
    """Cmdb/switch-controller.security-policy/802-1x connector."""

    uid = "name"
    _path = "api/v2/cmdb/switch-controller.security-policy/802-1X"
