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
from fortigate_api.types_ import LStr
from fortigate_api.virtual_ip import VirtualIP
from fortigate_api.zone import Zone


class FortigateAPI:
    """FortigateAPI, a set of connectors to work with commonly used fortigate-objects.

    Implemented Objects:

    :ivar obj address: :doc:`objects/Address`.
    :ivar obj address_group: :doc:`objects/AddressGroup`.
    :ivar obj antivirus: :doc:`objects/Antivirus`.
    :ivar obj application: :doc:`objects/Application`.
    :ivar obj dhcp_server: :doc:`objects/DhcpServer`.
    :ivar obj external_resource: :doc:`objects/ExternalResource`.
    :ivar obj interface: :doc:`objects/Interface`.
    :ivar obj internet_service: :doc:`objects/InternetService`.
    :ivar obj ip_pool: :doc:`objects/IpPool`.
    :ivar obj policy: :doc:`objects/Policy`.
    :ivar obj schedule: :doc:`objects/Schedule`.
    :ivar obj service: :doc:`objects/Service`.
    :ivar obj service_category: :doc:`objects/ServiceCategory`.
    :ivar obj service_group: :doc:`objects/ServiceGroup`.
    :ivar obj snmp_community: :doc:`objects/SnmpCommunity`.
    :ivar obj virtual_ip: :doc:`objects/VirtualIP`.
    :ivar obj zone: :doc:`objects/Zone`.
    """

    def __init__(self, **kwargs):  # TODO parameters as in netbox3
        """Init FortigateAPI.

        :param str host: Fortigate hostname or ip address.

        :param str username: Administrator name. Mutually exclusive with `token`.

        :param str password: Administrator password. Mutually exclusive with `token`.

        :param str token: Token. Mutually exclusive with `username` and `password`.

        :param str scheme: Access method: `https` or `http`. Default is `https`.

        :param int port: TCP port. Default is `443` for scheme=`https`, `80` for scheme=`http`.

        :param int timeout: Session timeout (minutes). Default is 15.

        :param bool verify: Transport Layer Security.
            `True` - A TLS certificate required,
            `False` - Requests will accept any TLS certificate.
            Default is `False`.

        :param str vdom: Name of the virtual domain. Default is `root`.
            This is only used in the REST API and not in SSH.

        :param dict ssh: Netmiko ConnectHandler parameters.
        """
        self.rest = Fortigate(**kwargs)
        self.ssh = SSH(**kwargs)
        # Object connectors
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
        """Login to the Fortigate using REST API.

        Used with `username` and `password` parameters, not used with `token`.
        """
        self.rest.login()
        return self

    def logout(self) -> None:
        """Logout from the Fortigate using REST API.

        Used with `username` and `password` parameters, not used with `token`.
        """
        self.rest.logout()

    @property
    def vdom(self) -> str:  # TODO rename to `active_vdom`
        """ACE TCP/UDP ports."""
        return self.rest.vdom

    @vdom.setter
    def vdom(self, vdom: str) -> None:
        vdom = str(vdom)
        if not vdom:
            vdom = VDOM
        self.rest.vdom = vdom

    # ============================= helpers ==============================

    def _get_connectors(self) -> LStr:
        """Return all Object connectors."""
        connectors: LStr = []
        for attr in dir(self):
            if attr in ["rest", "ssh"]:
                continue
            if attr.startswith("_"):
                continue
            obj = getattr(self, attr)
            if callable(obj):
                continue
            if callable(getattr(self, attr)):
                continue
            if getattr(FortigateAPI, attr, None):  # property
                continue
            connectors.append(attr)
        return connectors
