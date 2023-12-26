"""FortigateAPI, a set of connectors to work with commonly used objects."""

from __future__ import annotations

from fortigate_api.address import Address
from fortigate_api.address_group import AddressGroup
from fortigate_api.antivirus import Antivirus
from fortigate_api.application import Application
from fortigate_api.dhcp_server import DhcpServer
from fortigate_api.external_resource import ExternalResource
from fortigate_api.fortigate import Fortigate, HTTPS, TIMEOUT, VDOM
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
from fortigate_api.types_ import LStr, ODAny
from fortigate_api.vdoms import Vdoms
from fortigate_api.virtual_ip import VirtualIp
from fortigate_api.zone import Zone


class FortigateAPI:
    """FortigateAPI, a set of connectors to work with commonly used fortigate-objects."""

    def __init__(  # pylint: disable=too-many-arguments
            self,
            host: str,
            username: str = "",
            password: str = "",
            token: str = "",
            scheme: str = HTTPS,
            port: int = 0,
            timeout: int = TIMEOUT,
            verify: bool = False,
            vdom: str = VDOM,
            ssh: ODAny = None,
            **kwargs,
    ):
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
        kwargs = {
            "host": host,
            "username": username,
            "password": password,
            "token": token,
            "scheme": scheme,
            "port": port,
            "timeout": timeout,
            "verify": verify,
            "vdom": vdom,
            "ssh": ssh,
            **kwargs,
        }

        self.rest = Fortigate(**kwargs)
        """:py:class:`.Fortigate`"""

        self.ssh = SSH(**kwargs)
        """:py:class:`.SSH`"""

        # Object connectors

        self.address = Address(self.rest)
        """:py:class:`.Address`"""

        self.address_group = AddressGroup(self.rest)
        """:py:class:`.AddressGroup`"""

        self.antivirus = Antivirus(self.rest)
        """:py:class:`.Antivirus`"""

        self.application = Application(self.rest)
        """:py:class:`.Application`"""

        self.dhcp_server = DhcpServer(self.rest)
        """:py:class:`.DhcpServer`"""

        self.external_resource = ExternalResource(self.rest)
        """:py:class:`.ExternalResource`"""

        self.interface = Interface(self.rest)
        """:py:class:`.Interface`"""

        self.internet_service = InternetService(self.rest)
        """:py:class:`.InternetService`"""

        self.ip_pool = IpPool(self.rest)
        """:py:class:`.IpPool`"""

        self.policy = Policy(self.rest)
        """:py:class:`.Policy`"""

        self.schedule = Schedule(self.rest)
        """:py:class:`.Schedule`"""

        self.service = Service(self.rest)
        """:py:class:`.Service`"""

        self.service_category = ServiceCategory(self.rest)
        """:py:class:`.ServiceCategory`"""

        self.service_group = ServiceGroup(self.rest)
        """:py:class:`.ServiceGroup`"""

        self.snmp_community = SnmpCommunity(self.rest)
        """:py:class:`.SnmpCommunity`"""

        self.vdoms = Vdoms(self.rest)
        """:py:class:`.Vdoms`"""

        self.virtual_ip = VirtualIp(self.rest)
        """:py:class:`.VirtualIp`"""

        self.zone = Zone(self.rest)
        """:py:class:`.Zone`"""

    def __repr__(self):
        """Return a string representation related to this object."""
        return self.rest.__repr__()

    def __enter__(self):
        """Enter the runtime context.

        No need login REST and SSH. Session will be logged in after the first request.
        """
        return self

    def __exit__(self, *args):
        """Exit the runtime context, logout REST and SSH sessions."""
        self.rest.__exit__()
        self.ssh.__exit__()

    # ============================= property =============================

    @property
    def vdom(self) -> str:
        """Actual virtual domain."""
        return self.rest.vdom

    @vdom.setter
    def vdom(self, vdom: str) -> None:
        vdom = str(vdom)
        if not vdom:
            vdom = VDOM
        self.rest.vdom = vdom

    # =========================== methods ============================

    def login(self) -> FortigateAPI:
        """Login to the Fortigate using REST API and creates a Session object.

        - Validate `token` if object has been initialized with `token` parameter.
        - Validate  `password` if object has been initialized with `username` parameter.

        :return: None. Creates Session object.
        """
        self.rest.login()
        return self

    def logout(self) -> None:
        """Logout from the Fortigate using REST API, deletes Session object.

        - No need to logout if object has been initialized with `token` parameter.
        - Logout if object has been initialized with `username` parameter.

        :return: None. Deletes Session object
        """
        self.rest.logout()

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
