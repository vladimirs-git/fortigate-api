"""Fortigate API"""

from fortigate_api.address import Address
from fortigate_api.address_group import AddressGroup
from fortigate_api.antivirus import Antivirus
from fortigate_api.application import Application
from fortigate_api.fortigate import Fortigate
from fortigate_api.interface import Interface
from fortigate_api.internet_service import InternetService
from fortigate_api.ip_pool import IpPool
from fortigate_api.policy import Policy
from fortigate_api.schedule import Schedule
from fortigate_api.service import Service
from fortigate_api.service_category import ServiceCategory
from fortigate_api.service_group import ServiceGroup
from fortigate_api.snmp_community import SnmpCommunity
from fortigate_api.virtual_ip import VirtualIp
from fortigate_api.zone import Zone


class FortigateAPI:
    """Fortigate API"""

    def __init__(self, **kwargs):
        self.fgt = Fortigate(**kwargs)

        self.address = Address(fgt=self.fgt)
        self.address_group = AddressGroup(fgt=self.fgt)
        self.antivirus = Antivirus(fgt=self.fgt)
        self.application = Application(fgt=self.fgt)
        self.interface = Interface(fgt=self.fgt)
        self.internet_service = InternetService(fgt=self.fgt)
        self.ip_pool = IpPool(fgt=self.fgt)
        self.policy = Policy(fgt=self.fgt)
        self.schedule = Schedule(fgt=self.fgt)
        self.service = Service(fgt=self.fgt)
        self.service_category = ServiceCategory(fgt=self.fgt)
        self.service_group = ServiceGroup(fgt=self.fgt)
        self.snmp_community = SnmpCommunity(fgt=self.fgt)
        self.virtual_ip = VirtualIp(fgt=self.fgt)
        self.zone = Zone(fgt=self.fgt)

    def __repr__(self):
        return f"{self.fgt.host} vdom={self.fgt.vdom}"
