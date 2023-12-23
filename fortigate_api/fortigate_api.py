"""FortigateAPI, a set of connectors to work with commonly used objects."""

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
    """FortigateAPI, a set of connectors to work with commonly used objects.

    Connectors:

    :ivar obj address: :py:class:`fortigate_api.address.Address` :doc:`Address`.
    """

    def __init__(self, **kwargs):  # TODO parameters as in netbox3
        """Init FortigateAPI.

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
        self.rest = Fortigate(**kwargs)
        self.ssh = SSH(**kwargs)
        # Objects
        self.address = Address(self.rest)
        self.address_group = AddressGroup(self.rest)
        self.antivirus = Antivirus(self.rest)
        self.application = Application(self.rest)
        self.dhcp_server = DhcpServer(self.rest)
        self.external_resource = ExternalResource(self.rest)
        self.interface = Interface(self.rest)
        self.internet_service = InternetService(self.rest)
        self.ip_pool = IpPool(self.rest)
        self.policy = Policy(self.rest)
        self.schedule = Schedule(self.rest)
        self.service = Service(self.rest)
        self.service_category = ServiceCategory(self.rest)
        self.service_group = ServiceGroup(self.rest)
        self.snmp_community = SnmpCommunity(self.rest)
        self.virtual_ip = VirtualIP(self.rest)
        self.zone = Zone(self.rest)

    def __repr__(self):
        """Return a string representation related to this object."""
        return self.rest.__repr__()

    def __enter__(self):
        """Enter the runtime context related to this object."""
        return self

    def __exit__(self, *args):
        """Exit the runtime context related to this object."""
        self.rest.__exit__()
        self.ssh.__exit__()

    # =========================== methods ============================

    def login(self) -> FortigateAPI:
        """Login to the Fortigate using REST API."""
        self.rest.login()
        return self

    def logout(self) -> None:
        """Logout from the Fortigate using REST API."""
        self.rest.logout()

    @property
    def vdom(self) -> str:
        """ACE TCP/UDP ports."""
        return self.rest.vdom

    @vdom.setter
    def vdom(self, vdom: str) -> None:
        vdom = str(vdom)
        if not vdom:
            vdom = VDOM
        self.rest.vdom = vdom
