"""fortigate-api"""

from __future__ import annotations

from fortigate_api.address import Address
from fortigate_api.address_group import AddressGroup
from fortigate_api.antivirus import Antivirus
from fortigate_api.application import Application
from fortigate_api.dhcp_server import DhcpServer
from fortigate_api.external_resource import ExternalResource
from fortigate_api.fortigate import Fortigate, VDOM
from fortigate_api.interface import Interface
from fortigate_api.internet_service import InternetService
from fortigate_api.ip_pool import IpPool
from fortigate_api.policy import Policy
from fortigate_api.schedule import Schedule
from fortigate_api.service import Service
from fortigate_api.service_category import ServiceCategory
from fortigate_api.service_group import ServiceGroup
from fortigate_api.snmp_community import SnmpCommunity
from fortigate_api.ssh import SSH
from fortigate_api.virtual_ip import VirtualIP
from fortigate_api.zone import Zone


class FortigateAPI:
    """**FortigateAPI** - a set of methods for working with the most commonly used objects"""

    def __init__(self, **kwargs):
        """**FortigateAPI** - a set of methods for working with the most commonly used objects
        ::
            :param host: Firewall ip address or hostname
            :type host: str

            :param username: Administrator name. Mutually exclusive with token
            :type username: str

            :param password: Administrator password. Mutually exclusive with token
            :type password: str

            :param token: Administrator token. Mutually exclusive with username and password
            :type token: str

            :param scheme: (optional) "https" (default) or "http"
            :type scheme: str

            :param port: (optional) TCP port, by default 443 for "https", 80 for "http"
            :type port: str

            :param timeout: (optional) Session timeout minutes (default 15)
            :type timeout: int

            :param verify: (optional) Enable SSL certificate verification for HTTPS requests.
                True -  enable
                False - disable (default)
            :type verify: bool

            :param vdom: Name of virtual domain (default "root").
                Used in REST API (Not used in SSH)
            :type vdom: str

            :param ssh: Netmiko ConnectHandler parameters
            :type ssh: dict
        """
        self.fgt = Fortigate(**kwargs)
        self.ssh = SSH(**kwargs)

        self.address = Address(self.fgt)
        self.address_group = AddressGroup(self.fgt)
        self.antivirus = Antivirus(self.fgt)
        self.application = Application(self.fgt)
        self.dhcp_server = DhcpServer(self.fgt)
        self.external_resource = ExternalResource(self.fgt)
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

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.fgt.__exit__()
        self.ssh.__exit__()

    # =========================== methods ============================

    def login(self) -> FortigateAPI:
        """Login to the Fortigate using REST API """
        self.fgt.login()
        return self

    def logout(self) -> None:
        """Logout from the Fortigate using REST API"""
        self.fgt.logout()

    @property
    def vdom(self) -> str:
        """ACE TCP/UDP ports."""
        return self.fgt.vdom

    @vdom.setter
    def vdom(self, vdom: str) -> None:
        vdom = str(vdom)
        if not vdom:
            vdom = VDOM
        self.fgt.vdom = vdom
