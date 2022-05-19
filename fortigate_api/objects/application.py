"""Application Object"""

from fortigate_api.base.object_name import ObjectName


class Application(ObjectName):
    """Application Object"""

    def __init__(self, fgt):
        super().__init__(url_obj="api/v2/cmdb/application/list/", fgt=fgt)
