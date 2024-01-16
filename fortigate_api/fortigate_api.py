"""FortiGateAPI - Python connector to Fortigate API endpoints."""

from __future__ import annotations

from fortigate_api.cmdb.cmdb_s import CmdbS
from fortigate_api.fortigate import HTTPS, TIMEOUT, VDOM, FortiGate
from fortigate_api.log.log_s import LogS
from fortigate_api.monitor.monitor_s import MonitorS
from fortigate_api.types_ import LStr


class FortiGateAPI:
    """FortiGateAPI - Python connector to Fortigate API endpoints."""

    def __init__(
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
        logging: bool = False,
        logging_error: bool = False,
        **kwargs,
    ):
        """Init FortiGateAPI.

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

        :param bool logging: Logging REST API response.
            `Ture` - Enable response logging, `False` - otherwise. Default is `False`.

        :param bool logging_error: Logging only the REST API response with error.
            `Ture` - Enable errors logging, `False` - otherwise. Default is `False`.
        """
        api_params = {
            "host": host,
            "username": username,
            "password": password,
            "token": token,
            "scheme": scheme,
            "port": port,
            "timeout": timeout,
            "verify": verify,
            "vdom": vdom,
            "logging": logging,
            "logging_error": logging_error,
            **kwargs,
        }

        self.fortigate = FortiGate(**api_params)
        """:py:class:`.FortiGate` REST API connector."""

        self.cmdb = CmdbS(self.fortigate, **api_params)
        """:py:class:`.CmdbS` CMDB scope connectors."""

        self.log = LogS(self.fortigate, **api_params)  # todo LogS
        """:py:class:`.LogS` Log scope connectors. (not ready)"""

        self.monitor = MonitorS(self.fortigate, **api_params)  # todo MonitorS
        """:py:class:`.MonitorS` Monitor scope connectors. (not ready)"""

    def __repr__(self):
        """Return a string representation related to this object."""
        name = self.__class__.__name__
        host = self.fortigate.host
        return f"<{name}: {host}>"

    def __enter__(self):
        """Enter the runtime context related to this object."""
        self.fortigate.login()
        return self

    def __exit__(self, *args):
        """Exit the runtime context related to this object."""
        self.fortigate.logout()

    # ============================= property =============================

    @property
    def vdom(self) -> str:
        """Actual virtual domain."""
        return self.fortigate.vdom

    @vdom.setter
    def vdom(self, vdom: str) -> None:
        if not vdom:
            vdom = VDOM
        self.fortigate.vdom = str(vdom)

    # =========================== methods ============================

    def login(self) -> None:
        """Login to the Fortigate using REST API and creates a Session.

        - Validate `token` if object has been initialized with `token` parameter.
        - Validate  `password` if object has been initialized with `username` parameter.

        :return: None. Creates Session.
        """
        self.fortigate.login()

    def logout(self) -> None:
        """Logout from the Fortigate using REST API and deletes Session.

        - No need to logout if object has been initialized with `token` parameter.
        - Logout if object has been initialized with `username` parameter.

        :return: None. Deletes Session.
        """
        self.fortigate.logout()

    # ============================= helpers ==============================

    @staticmethod
    def _get_scopes() -> LStr:
        """Return all API scopes."""
        return ["cmdb", "log", "monitor"]
