"""Cmdb/firewall.service/category connector."""

from fortigate_api.connector import Connector


class CategoryFsC(Connector):
    """Cmdb/firewall.service/category connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall.service/category"
    _path_ui = "ng/firewall/service"
