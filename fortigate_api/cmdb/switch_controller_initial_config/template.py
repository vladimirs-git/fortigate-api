"""Cmdb/switch-controller.initial-config/template connector."""

from fortigate_api.connector import Connector


class TemplateScicC(Connector):
    """Cmdb/switch-controller.initial-config/template connector."""

    uid = "name"
    _path = "api/v2/cmdb/switch-controller.initial-config/template"
