"""ServiceGroup Object"""

from fortigate_api.base.object_name import ObjectName


class ServiceGroup(ObjectName):
    """ServiceGroup Object"""

    def __init__(self, fgt):
        super().__init__(url_obj="api/v2/cmdb/firewall.service/group/", fgt=fgt)
