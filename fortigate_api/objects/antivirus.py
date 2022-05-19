"""Antivirus Object"""

from fortigate_api.base.object_name import ObjectName


class Antivirus(ObjectName):
    """Antivirus Object"""

    def __init__(self, fgt):
        super().__init__(url_obj="api/v2/cmdb/antivirus/profile/", fgt=fgt)
