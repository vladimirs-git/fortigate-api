"""Cmdb/wireless-controller/apcfg-profile connector."""

from fortigate_api.connector import Connector


class ApcfgProfileWcC(Connector):
    """Cmdb/wireless-controller/apcfg-profile connector."""

    uid = "name"
    _path = "api/v2/cmdb/wireless-controller/apcfg-profile"
