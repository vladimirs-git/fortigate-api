"""Cmdb/system/custom-language connector."""

from fortigate_api.connector import Connector


class CustomLanguageSC(Connector):
    """Cmdb/system/custom-language connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/custom-language"
