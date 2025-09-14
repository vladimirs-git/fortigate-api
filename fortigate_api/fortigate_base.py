"""Base for FortiGate, set of private methods."""

from __future__ import annotations

import ipaddress
import json
import logging
from typing import Callable, Iterable, Optional
from urllib.parse import urlencode, urljoin, urlunparse

import requests
from requests import Session, Response
from requests.exceptions import SSLError
from requests.packages import urllib3  # type: ignore

from fortigate_api import helpers as h
from fortigate_api.types_ import DAny, ODAny, DStr, Method

# noinspection PyUnresolvedReferences
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HTTP = "http"
HTTPS = "https"
PORT_443 = 443
PORT_80 = 80
TIMEOUT = 15
VDOM = "root"


class FortiGateBase:
    """Base for FortiGate, set of private methods."""

    # noinspection PyShadowingNames
    def __init__(self, **kwargs):
        """Init FortiGateBase.

        :param str host: Fortigate hostname or ip address.

        :param str username: Administrator name. Mutually exclusive with `token`.

        :param str password: Administrator password. Mutually exclusive with `token`.

        :param str token: Token. Mutually exclusive with `username` and `password`.

        :param str scheme: Access method: `https` or `http`. Default is `https`.

        :param int port: TCP port. Default is `443` for scheme=`https`, `80` for scheme=`http`.

        :param int timeout: Session timeout (minutes). Default is 15.

        :param bool verify: Transport Layer Security.
            `True` - A TLS certificate required,
            `False` - Requests will accept any TLS certificate. Default is `False`.

        :param str vdom: Name of the virtual domain. Default is `root`.

        :param bool logging: Logging REST API response.
            `True` - Enable response logging, `False` - otherwise. Default is `False`.

        :param bool logging_error: Logging only the REST API response with error.
            `True` - Enable errors logging, `False` - otherwise. Default is `False`.
        """
        self.host = _init_host(**kwargs)
        self.username = str(kwargs.get("username"))
        self.password = str(kwargs.get("password"))
        self.token = _init_token(**kwargs)
        self.scheme: str = _init_scheme(**kwargs)
        self.port: int = self._init_port(**kwargs)
        self.timeout: int = int(kwargs.get("timeout") or 0)
        self.vdom: str = str(kwargs.get("vdom") or VDOM)
        self.verify: bool = bool(kwargs.get("verify"))
        # logging
        self.logging: bool = bool(kwargs.get("logging"))
        self.logging_error: bool = bool(kwargs.get("logging_error"))
        if self.logging_error:
            self.logging = True

        self._session: Optional[Session] = None

    def __repr__(self):
        """Return a string representation related to this object."""
        host = self.host
        username = self.username
        scheme = self.scheme
        port = self.port
        timeout = self.timeout
        verify = self.verify
        vdom = self.vdom
        params = [
            f"{host=!r}",
            f"{username=!r}",
        ]
        params_optional = [
            f"{scheme=!r}" if scheme != HTTPS else "",
            f"{port=!r}" if port else "",
            f"{timeout=!r}" if timeout != TIMEOUT else "",
            f"{verify=!r}" if verify is True else "",
            f"{vdom=!r}" if vdom != VDOM else "",
        ]
        params.extend([s for s in params_optional if s])
        params_ = ", ".join([s for s in params if s])
        return f"{self.__class__.__name__}({params_})"

    def __enter__(self):
        """Enter the runtime context related to this object."""
        self.login()
        return self

    def __exit__(self, *args):
        """Exit the runtime context related to this object."""
        self.logout()

    # =========================== property ===========================

    @property
    def is_connected(self) -> bool:
        """Check connection to the Fortigate.

        :return: True if the session is connected to the Fortigate, False otherwise.
        :rtype: bool
        """
        return isinstance(self._session, Session)

    @property
    def url(self) -> str:
        """Return URL to the Fortigate."""
        components = (self.scheme, f"{self.host}:{self.port}", "/", "", "", "")
        return urlunparse(components)

    # ============================ login =============================

    def login(self) -> None:
        """Login to the Fortigate using REST API and creates a Session object.

        - Validate `token` if object has been initialized with `token` parameter.
        - Validate `password` if object has been initialized with `username` parameter.

        :return: None. Creates Session object.
        """
        session: Session = requests.session()

        # token
        if self.token:
            try:
                response: Response = session.get(
                    url=urljoin(self.url, "/api/v2/monitor/system/status"),
                    headers=self._bearer_token(),
                    verify=self.verify,
                )
            except Exception as ex:
                raise self._hide_secret_ex(ex)
            response.raise_for_status()
            self._session = session
            return

        # password
        try:
            response = session.post(
                url=urljoin(self.url, "/logincheck"),
                data=urlencode([("username", self.username), ("secretkey", self.password)]),
                timeout=self.timeout,
                verify=self.verify,
            )
        except Exception as ex:
            raise self._hide_secret_ex(ex)
        response.raise_for_status()
        token = self._get_token_from_cookies(session)
        session.headers.update({"X-CSRFTOKEN": token})
        self._session = session

    def logout(self) -> None:
        """Logout from the Fortigate using REST API, deletes Session object.

        - No need to logo ut if object has been initialized with `token` parameter.
        - Log out if object has been initialized with `username` parameter.

        :return: None. Deletes Session object
        """
        if isinstance(self._session, Session):
            if not self.token:
                try:
                    self._session.get(
                        url=urljoin(self.url, "/logout"),
                        timeout=self.timeout,
                        verify=self.verify,
                    )
                except SSLError:
                    pass
        self._session = None

    # =========================== helpers ============================

    def _bearer_token(self) -> DStr:
        """Return bearer token."""
        return {"Authorization": f"Bearer {self.token}"}

    def get_session(self) -> Session:
        """Return an existing session or create a new one."""
        if not self.is_connected:
            self.login()
        session = self._session
        if not isinstance(session, Session):
            raise TypeError(f"{Session.__name__} expected.")
        return session

    @staticmethod
    def _get_token_from_cookies(session: Session) -> str:
        """Retrieve the token from the cookies in the session.

        Look for a cookie that is named `ccsrftoken` or stars with `ccsrftoken_`.

        :param session: The session object containing cookies.

        :return: The token extracted from the cookies.

        :raises ValueError: If the ccsrftoken cookie is absent.
        """
        cookie_prefix = "ccsrftoken"
        if cookies := [o for o in session.cookies if o and o.name.startswith(cookie_prefix)]:
            token = str(cookies[0].value)
            token = token.strip('"')
            return token
        raise ValueError("Invalid login credentials. Cookie 'ccsrftoken' is missing.")

    def _hide_secret(self, string: str) -> str:
        """Hide password, secretkey in text (for safe logging)."""
        if not self.password:
            return string
        result = string.replace(self.password, "<hidden>")
        quoted_password = h.quote(self.password)
        result = result.replace(quoted_password, "<hidden>")
        return result

    def _hide_secret_ex(self, ex):
        """Hide secretkey in exception (for safe logging)."""
        if hasattr(ex, "args"):
            if (args := getattr(ex, "args")) and isinstance(args, Iterable):
                msgs = []  # result
                for arg in args:
                    if isinstance(arg, str):
                        msgs.append(self._hide_secret(string=arg))
                    else:
                        msgs.append(arg)
                return type(ex)(tuple(msgs))
        return ex

    def _init_port(self, **kwargs) -> int:
        """Init port, 443 for scheme=`https`, 80 for scheme=`http`."""
        if port := int(kwargs.get("port") or 0):
            return port
        if self.scheme == HTTP:
            return PORT_80
        return PORT_443

    def _logging(self, resp: Response) -> None:
        """Log response."""
        if not self.logging:
            return
        if self.logging_error and resp.ok:
            return
        code = resp.status_code
        reason = resp.reason
        url = self._hide_secret(string=resp.url)
        msg = f"{code=} {reason=} {url=}"
        logging.info(msg)
        logging.debug("text=%s", resp.text)

    def _response(self, method: Method, url: str, data: ODAny = None) -> Response:
        """Call Session method and return Response.

        :param str method: Session method: `delete`, `get`, `post`, `put`.

        :param str url: REST API URL to the fortigate-object.

        :param data: Data of the fortigate-object.

        :return: Session response.
        :rtype: Response
        """
        params: DAny = {
            "url": urljoin(self.url, url),
            "params": urlencode([("vdom", self.vdom)]),
            "timeout": self.timeout,
            "verify": self.verify,
        }
        if isinstance(data, dict):
            params["data"] = json.dumps(data)
        if self.token:
            params["headers"] = self._bearer_token()

        session: Session = self.get_session()
        method_: Callable = getattr(session, method)
        try:
            response: Response = method_(**params)
        except Exception as ex:
            raise self._hide_secret_ex(ex)
        return response


# =========================== helpers ============================


def _init_host(**kwargs) -> str:
    """Init host: valid hostname or valid IPv4/IPv6 address."""
    host = str(kwargs.get("host", "")).strip()
    if not host:
        raise ValueError(f"{host=!r}, hostname is not specified.")

    # Strip brackets if provided (IPv6 URL style)
    if host.startswith("[") and host.endswith("]"):
        host = host[1:-1]

    # Try IP validation first
    try:
        ip = ipaddress.ip_address(host)
        if isinstance(ip, ipaddress.IPv6Address):
            host = f"[{host}]"
    except ValueError:
        pass  # hostname

    return host


def _init_scheme(**kwargs) -> str:
    """Init scheme `https` or `http`."""
    scheme = str(kwargs.get("scheme") or HTTPS)
    expected = [HTTPS, HTTP]
    if scheme not in expected:
        raise ValueError(f"{scheme=!r}, {expected=!r}.")
    return scheme


def _init_token(**kwargs) -> str:
    """Init token."""
    token = str(kwargs.get("token") or "")
    if not token:
        return ""
    if kwargs.get("username"):
        raise ValueError("A username and a token are mutually exclusive.")
    if kwargs.get("password"):
        raise ValueError("A password and a token are mutually exclusive.")
    return token
