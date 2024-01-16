"""Cmdb/system/object-tagging connector."""

from fortigate_api.connector import Connector


class ObjectTaggingSC(Connector):
    """Cmdb/system/object-tagging connector."""

    uid = "category"
    _path = "api/v2/cmdb/system/object-tagging"
