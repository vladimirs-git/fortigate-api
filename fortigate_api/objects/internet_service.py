"""InternetService Object"""

from fortigate_api.base.object_name import ObjectName

URL = "api/v2/cmdb/firewall/internet-service/"


class InternetService(ObjectName):
    """InternetService Object"""

    def __init__(self, fgt):
        super().__init__(url_obj="api/v2/cmdb/firewall/internet-service/", fgt=fgt)
