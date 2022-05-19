"""Zone Object"""

from fortigate_api.base.object_name import ObjectName
from fortigate_api.objects.interface import Interface
from fortigate_api.types_ import LDAny, LStr


class Zone(ObjectName):
    """Zone Object"""

    def __init__(self, fgt):
        super().__init__(url_obj="api/v2/cmdb/system/zone/", fgt=fgt)

    def get(self, **kwargs) -> LDAny:
        """Gets zone-objects in vdom, all or filtered by params: name, filter, filters"""
        interface_o = Interface(fgt=self.fgt)
        interfaces: LStr = [d["name"] for d in interface_o.get()]
        zones_all: LDAny = self._get(url=self.url_obj, **kwargs)
        zones: LDAny = list()
        for zone in zones_all:
            for intf_d in zone["interface"]:
                if intf_d["interface-name"] in interfaces:
                    zones.append(zone)
                    break
        return zones

    def get_all(self) -> LDAny:
        """Gets zone-objects, all"""
        return self._get(url=self.url_obj)
