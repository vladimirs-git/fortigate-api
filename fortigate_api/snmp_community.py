"""SNMP Community Object"""

from fortigate_api.base import Base


class SnmpCommunity(Base):
    """SNMP Community Object"""

    def __init__(self, fgt):
        super().__init__(fgt=fgt, url_obj="api/v2/cmdb/system.snmp/community/", uid_key="id")
