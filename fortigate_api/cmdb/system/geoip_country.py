"""Cmdb/system/geoip-country connector."""

from fortigate_api.connector import Connector


class GeoipCountrySC(Connector):
    """Cmdb/system/geoip-country connector."""

    uid = "id"
    _path = "api/v2/cmdb/system/geoip-country"
