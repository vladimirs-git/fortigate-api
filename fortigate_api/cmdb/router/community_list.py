"""Cmdb/router/community-list connector."""

from fortigate_api.connector import Connector


class CommunityListRC(Connector):
    """Cmdb/router/community-list connector."""

    uid = "name"
    _path = "api/v2/cmdb/router/community-list"
