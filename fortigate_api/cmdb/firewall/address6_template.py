"""Cmdb/firewall/address6-template connector."""

from fortigate_api.connector import Connector


class Address6TemplateFC(Connector):
    """Cmdb/firewall/address6-template connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/address6-template"
