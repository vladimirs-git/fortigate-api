"""SNMP Community Object"""

from fortigate_api.base.object_id import ObjectID


class SnmpCommunity(ObjectID):
    """SNMP Community Object"""

    def __init__(self, fgt):
        super().__init__(url_obj="api/v2/cmdb/system.snmp/community/", fgt=fgt)
