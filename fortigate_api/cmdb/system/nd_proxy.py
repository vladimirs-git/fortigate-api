"""Cmdb/system/nd-proxy connector."""

from fortigate_api.connector import Connector


class NdProxySC(Connector):
    """Cmdb/system/nd-proxy connector."""

    uid = ""
    _path = "api/v2/cmdb/system/nd-proxy"
