"""Cmdb/webfilter/ftgd-local-rating connector."""

from fortigate_api.connector import Connector


class FtgdLocalRatingWC(Connector):
    """Cmdb/webfilter/ftgd-local-rating connector."""

    uid = "url"
    _path = "api/v2/cmdb/webfilter/ftgd-local-rating"
