"""Cmdb/vpn.ipsec/forticlient connector."""

from fortigate_api.connector import Connector


class ForticlientViC(Connector):
    """Cmdb/vpn.ipsec/forticlient connector."""

    uid = "realm"
    _path = "api/v2/cmdb/vpn.ipsec/forticlient"
