"""InternetService Object"""

from fortigate_api.base import Base


class InternetService(Base):
    """InternetService Object"""

    def __init__(self, fgt):
        super().__init__(fgt=fgt, url_obj="api/v2/cmdb/firewall/internet-service/")
