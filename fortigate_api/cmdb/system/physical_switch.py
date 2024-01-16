"""Cmdb/system/physical-switch connector."""

from fortigate_api.connector import Connector


class PhysicalSwitchSC(Connector):
    """Cmdb/system/physical-switch connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/physical-switch"
