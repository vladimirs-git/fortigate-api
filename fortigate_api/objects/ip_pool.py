"""IpPool Object"""

from fortigate_api.base.object_name import ObjectName


class IpPool(ObjectName):
    """IpPool Object"""

    def __init__(self, fgt):
        super().__init__(url_obj="api/v2/cmdb/firewall/ippool/", fgt=fgt)
