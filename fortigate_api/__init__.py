"""fortigate-api"""

from requests import Session

from fortigate_api.fortigate import Fortigate
from fortigate_api.address import Address
from fortigate_api.address_group import AddressGroup
from fortigate_api.antivirus import Antivirus
from fortigate_api.application import Application
from fortigate_api.interface import Interface
from fortigate_api.internet_service import InternetService
from fortigate_api.ip_pool import IpPool
from fortigate_api.policy import Policy
from fortigate_api.schedule import Schedule
from fortigate_api.service import Service
from fortigate_api.service_category import ServiceCategory
from fortigate_api.service_group import ServiceGroup
from fortigate_api.snmp_community import SnmpCommunity
from fortigate_api.virtual_ip import VirtualIP
from fortigate_api.zone import Zone

__all__ = [
    "Fortigate",
    "FortigateAPI",
]

__version__ = "0.2.0"
__date__ = "2022-05-21"
__title__ = "fortigate-api"

__summary__ = "Python package to configure Fortigate (Fortios) devices using REST API"
__author__ = "Vladimir Prusakov"
__email__ = "vladimir.prusakovs@gmail.com"
__url__ = "https://github.com/vladimirs-git/fortigate-api"
__download_url__ = f"{__url__}/archive/refs/tags/{__version__}.tar.gz"
__license__ = "MIT"


class FortigateAPI:
    """**FortigateAPI** - a set of methods for working with the most commonly used objects"""

    def __init__(self, **kwargs):
        """**FortigateAPI** - a set of methods for working with the most commonly used objects
        :param host: Firewall ip address or hostname
        :param username: Administrator name
        :param password: Administrator password
        :param port: HTTPS port, by default 443
        :param timeout: Session timeout (minutes), by default 15
        :param vdom: Name of virtual domain, by default "root"
        """
        self.fgt = Fortigate(**kwargs)

        self.address = Address(self.fgt)
        self.address_group = AddressGroup(self.fgt)
        self.antivirus = Antivirus(self.fgt)
        self.application = Application(self.fgt)
        self.interface = Interface(self.fgt)
        self.internet_service = InternetService(self.fgt)
        self.ip_pool = IpPool(self.fgt)
        self.policy = Policy(self.fgt)
        self.schedule = Schedule(self.fgt)
        self.service = Service(self.fgt)
        self.service_category = ServiceCategory(self.fgt)
        self.service_group = ServiceGroup(self.fgt)
        self.snmp_community = SnmpCommunity(self.fgt)
        self.virtual_ip = VirtualIP(self.fgt)
        self.zone = Zone(self.fgt)

    def __repr__(self):
        return self.fgt.__repr__()

    # =========================== methods ============================

    def login(self) -> Session:
        """Login to Fortigate"""
        return self.fgt.login()

    def logout(self) -> None:
        """Logout Fortigate"""
        self.fgt.logout()
