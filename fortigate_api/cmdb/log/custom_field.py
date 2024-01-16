"""Cmdb/log/custom-field connector."""

from fortigate_api.connector import Connector


class CustomFieldLC(Connector):
    """Cmdb/log/custom-field connector."""

    uid = "id"
    _path = "api/v2/cmdb/log/custom-field"
