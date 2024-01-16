"""Cmdb/dlp/fp-doc-source connector."""

from fortigate_api.connector import Connector


class FpDocSourceDC(Connector):
    """Cmdb/dlp/fp-doc-source connector."""

    uid = "name"
    _path = "api/v2/cmdb/dlp/fp-doc-source"
