"""Cmdb/system/geoip-override connector."""

from fortigate_api.connector import Connector


class GeoipOverrideSC(Connector):
    """Cmdb/system/geoip-override connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/geoip-override"
