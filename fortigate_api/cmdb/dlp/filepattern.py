"""Cmdb/dlp/filepattern connector."""

from fortigate_api.connector import Connector


class FilepatternDC(Connector):
    """Cmdb/dlp/filepattern connector."""

    uid = "id"
    _path = "api/v2/cmdb/dlp/filepattern"
