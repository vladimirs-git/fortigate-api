"""Fortigate, REST API connector to the Fortigate."""
from __future__ import annotations

import json
import logging
import re
from typing import Callable, Iterable, Optional
from urllib.parse import urlencode, urljoin

import requests
from requests import Session, Response
from requests.exceptions import SSLError
from requests.packages import urllib3  # type: ignore

from fortigate_api import helpers as h
from fortigate_api.types_ import DAny, LDAny, ODAny, DStr, Method

# noinspection PyUnresolvedReferences
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HTTPS = "https"
PORT_443 = 443
PORT_80 = 80
TIMEOUT = 15
VDOM = "root"


class Fortigate:
    """Fortigate, REST API connector to the Fortigate.

    A set of methods to work with any objects available through the REST API.
    Is useful for working with objects that are not implemented in :py:class:`.FortigateAPI`.
    """

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
            **kwargs,
    ):
        """Init Fortigate.

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
            This is only used in the REST API and not in SSH.
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
            **kwargs,
        }

        self.host = str(host)
        self.username = str(kwargs.get("username"))
        self.password = str(kwargs.get("password"))
        self.token = _init_token(**kwargs)
        self.scheme: str = _init_scheme(**kwargs)
        self.port: int = self._init_port(**kwargs)
        self.timeout: int = int(kwargs.get("timeout") or 0)
        self.vdom: str = str(kwargs.get("vdom") or VDOM)
        self.verify: bool = bool(kwargs.get("verify"))

        self._session: Optional[Session] = None

    def __repr__(self):
        """Return a string representation related to this object."""
        host = self.host
        username = self.username
        scheme = self.scheme
        port = self.port if not (scheme == HTTPS and self.port == PORT_443) else ""
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
        if self.scheme == HTTPS and self.port == 443:
            return f"{self.scheme}://{self.host}"
        if self.scheme == "http" and self.port == 80:
            return f"{self.scheme}://{self.host}"
        return f"{self.scheme}://{self.host}:{self.port}"

    # ============================ login =============================

    def login(self) -> None:
        """Login to the Fortigate using REST API and creates a Session object.

        - Validate 'token' if object has been initialized with `token` parameter.
        - Validate  `password` if object has been initialized with `username` parameter.

        :return: None. Creates Session object.
        """
        session: Session = requests.session()

        # token
        if self.token:
            try:
                response: Response = session.get(
                    url=f"{self.url}/api/v2/cmdb/system/status",
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
            session.post(
                url=f"{self.url}/logincheck",
                data=urlencode([("username", self.username), ("secretkey", self.password)]),
                timeout=self.timeout,
                verify=self.verify,
            )
        except Exception as ex:
            raise self._hide_secret_ex(ex)

        token = self._get_token_from_cookies(session)
        session.headers.update({"X-CSRFTOKEN": token})

        response = session.get(url=f"{self.url}/api/v2/cmdb/system/vdom")
        response.raise_for_status()
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
                    self._session.get(url=f"{self.url}/logout",
                                      timeout=self.timeout,
                                      verify=self.verify)
                except SSLError:
                    pass
            del self._session
        self._session = None

    # =========================== methods ============================

    def delete(self, url: str) -> Response:
        """DELETE the fortigate-object from the Fortigate.

        :param str url: REST API URL to the fortigate-object.

        :return: Session response.

            - `<Response [200]>` Object successfully deleted,
            - `<Response [400]>` Invalid URL,
            - `<Response [404]>` Object not found in the Fortigate.
        :rtype: requests.Response
        """
        response: Response = self._response("delete", url)
        if not response.ok:
            self._logging(response)
        return response

    def get(self, url: str) -> LDAny:
        """GET fortigate-object from the Fortigate.

        Fortigate returns dictionary with key="results".

        :param url url: REST API URL to the fortigate-objects.

        :return: List of the fortigate-objects.
        :rtype: List[dict]
        """
        response: Response = self._response("get", url)
        if not response.ok:
            logging.info("code=%s, reason=%s, url=%s", response.status_code, response.reason, url)
            return []
        response_json = response.json()
        results: LDAny = list(response_json.get("results") or [])
        return results

    def get_l(self, url: str) -> list:
        """GET list of the fortigate-objects from the Fortigate.

        Fortigate returns list of the items.

        :param str url: REST API URL to the fortigate-objects.

        :return: List of the items.
        :rtype: List[dict]
        """
        response: Response = self._response("get", url)
        if not response.ok:
            logging.info("code=%s, reason=%s, url=%s", response.status_code, response.reason, url)
            return []
        results: LDAny = list(response.json() or [])
        return results

    def post(self, url: str, data: DAny) -> Response:
        """POST (create) fortigate-object in the Fortigate based on the data.

        :param str url: REST API URL to the fortigate-object.

        :param dict data: Data of the fortigate-object.

        :return: Session response.

            - `<Response [200]>` Object successfully created or already exists,
            - `<Response [400]>` Invalid URL,
            - `<Response [500]>` Object already exist.
        :rtype: requests.Response
        """
        response: Response = self._response("post", url, data)
        if not response.ok:
            self._logging(response)
        return response

    def put(self, url: str, data: DAny) -> Response:
        """PUT (update) existing fortigate-object in the Fortigate.

        :param str url: REST API URL to the fortigate-object.

        :param dict data: Data of the fortigate-object.

        :return: Session response.

            - `Response [200]>` Object successfully updated,
            - `Response [400]>` Invalid URL,
            - `Response [404]>` Object has not been updated.
        :rtype: requests.Response
        """
        response: Response = self._response("put", url, data)
        if not response.ok:
            self._logging(response)
        return response

    def directory(self, url: str) -> LDAny:
        """Get directory schema of available REST API data source.

        :param str url: REST API URL to the directory.

        :return: List of the fortigate-objects.
        :rtype: List[dict]
        """
        response: Response = self._response("get", url)
        if not response.ok:
            logging.info("code=%s, reason=%s, url=%s", response.status_code, response.reason, url)
            return []
        response_json = response.json()
        results: LDAny = response_json.get("directory") or []
        return results

    def exist(self, url: str) -> Response:
        """Check if a fortigate-object exists in the Fortigate.

        :param str url: REST API URL to the fortigate-object.

        :return: Session response.

            - `<Response [200]>` Object exist,
            - `Response [400]>` Invalid URL,
            - `<Response [404]>` Object does not exist.
        :rtype: requests.Response
        """
        return self._response("get", url)

    # =========================== helpers ============================

    def _bearer_token(self) -> DStr:
        """Return bearer token."""
        return {"Authorization": f"Bearer {self.token}"}

    def _get_session(self) -> Session:
        """Return an existing session or create a new one."""
        if not self.is_connected:
            self.login()
        session = self._session
        if not isinstance(session, Session):
            raise TypeError(f"{session=} {Session} expected.")
        return session

    @staticmethod
    def _get_token_from_cookies(session: Session) -> str:
        """Retrieve the token from the cookies in the session.

        Look for a cookie that is named `ccsrftoken` or stars with `ccsrftoken_`.

        :param session: The session object containing cookies.

        :return: The token extracted from the cookies.

        :raises ValueError: If the ccsrftoken cookie is absent.
        """
        while True:
            # fortios < v7
            cookie_name = "ccsrftoken"
            if cookies := [o for o in session.cookies if o and o.name == cookie_name]:
                break

            # fortios >= v7
            cookie_name += "_"
            if cookies := [o for o in session.cookies if o and o.name.startswith(cookie_name)]:
                break

            raise ValueError("Invalid login credentials. Cookie 'ccsrftoken' is missing.")

        token = str(cookies[0].value).strip("\"")
        return token

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
        if self.scheme == "http":
            return PORT_80
        return PORT_443

    def _logging(self, resp: Response) -> None:
        """Log response."""
        code = resp.status_code
        reason = resp.reason
        url = self._hide_secret(string=resp.url)
        msg = f"{code=} {reason=} {url=}"
        logging.info(msg)
        if logging.getLogger().level <= logging.DEBUG:
            logging.debug("text=%s", resp.text)

    def _response(self, method: Method, url: str, data: ODAny = None) -> Response:
        """Call Session method and return Response.

        :param str method: Session method: `delete`, `get`, `post`, `put`.

        :param str url: REST API URL to the fortigate-object.

        :param data: Data of the fortigate-object.

        :return: Session response.
        :rtype: requests.Response
        """
        params: DAny = {
            "url": self._valid_url(url),
            "params": urlencode([("vdom", self.vdom)]),
            "timeout": self.timeout,
            "verify": self.verify,
        }
        if isinstance(data, dict):
            params["data"] = json.dumps(data)
        if self.token:
            params["headers"] = self._bearer_token()

        session: Session = self._get_session()
        method_: Callable = getattr(session, method)
        try:
            response: Response = method_(**params)
        except Exception as ex:
            raise self._hide_secret_ex(ex)
        return response

    def _valid_url(self, url: str) -> str:
        """Return a valid URL string.

        Add `https://` to `url` if it is absent and remove trailing `/` character.
        """
        if re.match("http(s)?://", url):
            return url.rstrip("/")
        path = url.strip("/")
        return urljoin(self.url, path)


def _init_scheme(**kwargs) -> str:
    """Init scheme `https` or `http`."""
    scheme = str(kwargs.get("scheme") or HTTPS)
    expected = ["https", "http"]
    if scheme not in expected:
        raise ValueError(f"{scheme=}, {expected=}.")
    return scheme


def _init_token(**kwargs) -> str:
    """Init token."""
    token = str(kwargs.get("token") or "")
    if not token:
        return ""
    if kwargs.get("username"):
        raise ValueError("Mutually excluded: username, token.")
    if kwargs.get("password"):
        raise ValueError("Mutually excluded: password, token.")
    return token