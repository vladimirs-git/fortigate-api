"""Schedule Object"""

from fortigate_api.base import Base


class Schedule(Base):
    """Schedule Object"""

    def __init__(self, fgt):
        super().__init__(fgt=fgt, url_obj="api/v2/cmdb/firewall.schedule/onetime/")
