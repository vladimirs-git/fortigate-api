"""Cmdb/wireless-controller.hotspot20/anqp-venue-name connector."""

from fortigate_api.connector import Connector


class AnqpVenueNameWchC(Connector):
    """Cmdb/wireless-controller.hotspot20/anqp-venue-name connector."""

    uid = "name"
    _path = "api/v2/cmdb/wireless-controller.hotspot20/anqp-venue-name"
