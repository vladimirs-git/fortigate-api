"""**Fortigate(host, username, password, scheme, port, timeout, vdom)**.

REST API connector to the Fortigate. Contains generic methods (get, put, delete, etc.)
to work with any objects available through the REST API. `Fortigate`_ is useful for working with
objects that are not implemented in `FortigateAPI`_
"""
from __future__ import annotations

import json
import logging
import re
from typing import Callable, Iterable, Optional
from urllib.parse import urlencode

import requests
from requests import Session, Response
from requests.exceptions import SSLError
from requests.packages import urllib3  # type: ignore

from fortigate_api import helpers as h
from fortigate_api.types_ import DAny, LDAny, DStr, Method

# noinspection PyUnresolvedReferences
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HTTPS = "https"
PORT_443 = 443
PORT_80 = 80
TIMEOUT = 15
VDOM = "root"


class Fortigate:
    """**Fortigate(host, username, password, scheme, port, timeout, vdom)**.

    REST API connector to the Fortigate. Contains generic methods (get, put, delete, etc.)
    to work with any objects available through the REST API. `Fortigate`_ is useful for working with
    objects that are not implemented in `FortigateAPI`_
    """

    def __init__(self, host: str, **kwargs):
        """**Fortigate** - Firewall Connector.

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

            :param vdom: Name of virtual domain (default "root")
            :type vdom: str
        """
        self.host = host
        self.username = str(kwargs.get("username") or "")
        self.password = str(kwargs.get("password") or "")
        self.token = self._init_token(**kwargs)
        self.scheme: str = self._init_scheme(**kwargs)
        self.port: int = self._init_port(**kwargs)
        self.timeout: int = int(kwargs.get("timeout") or TIMEOUT)
        self.vdom: str = str(kwargs.get("vdom") or VDOM)
        self.verify: bool = bool(kwargs.get("verify") or False)
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

    # ============================= init =============================

    def _init_port(self, **kwargs) -> int:
        """Init port, 443 for "https", 80 for "http"."""
        if port := int(kwargs.get("port") or 0):
            return port
        if self.scheme == "http":
            return PORT_80
        return PORT_443

    @staticmethod
    def _init_scheme(**kwargs) -> str:
        """Init scheme "https" or "http"."""
        scheme = str(kwargs.get("scheme") or HTTPS)
        expected = ["https", "http"]
        if scheme not in expected:
            raise ValueError(f"{scheme=}, {expected=}")
        return scheme

    def _init_token(self, **kwargs) -> str:
        """Init token."""
        token = str(kwargs.get("token") or "")
        if not token:
            return ""
        if self.username:
            raise ValueError("mutually excluded: username, token")
        if self.password:
            raise ValueError("mutually excluded: password, token")
        return token

    # =========================== property ===========================

    @property
    def is_connected(self) -> bool:
        """Check connection to the Fortigate.

        ::
            :return: True if session is connected to the Fortigate
            :rtype: bool
        """
        return isinstance(self._session, Session)

    @property
    def url(self) -> str:
        """Return URL to the Fortigate."""
        if self.port == 443:
            return f"{self.scheme}://{self.host}"
        return f"{self.scheme}://{self.host}:{self.port}"

    # ============================ login =============================

    def login(self) -> None:
        """Login to the Fortigate using REST API, creates Session object.

        ::
            :return: None. Creates Session object
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

        # username
        try:
            session.post(
                url=f"{self.url}/logincheck",
                data=urlencode([("username", self.username), ("secretkey", self.password)]),
                timeout=self.timeout,
                verify=self.verify,
            )
        except Exception as ex:
            raise self._hide_secret_ex(ex)

        cookie_name = "ccsrftoken"
        cookies = [o for o in session.cookies if o and o.name == cookie_name]
        if not cookies:
            regex = cookie_name + r"_\d+$"
            cookies = [o for o in session.cookies if re.match(regex, o.name)]
        cookies = [o for o in cookies if isinstance(o.value, str)]
        if not cookies:
            raise ValueError("invalid login credentials, absent cookie ccsrftoken")
        cookie = cookies[0]
        token = str(cookie.value).strip("\"")
        session.headers.update({"X-CSRFTOKEN": token})

        response = session.get(url=f"{self.url}/api/v2/cmdb/system/vdom")
        response.raise_for_status()
        self._session = session

    def logout(self) -> None:
        """Logout from the Fortigate using REST API, deletes Session object.

        ::
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
        """DELETE object from the Fortigate.

        ::
            :param url: REST API URL to the object
            :type url: str

            :return: Session response
                *<Response [200]>* Object successfully deleted
                *<Response [404]>* Object absent in the Fortigate
            :rtype: Response
        """
        response: Response = self._response("delete", url)
        if not response.ok:
            self._logging(response)
        return response

    def directory(self, url: str) -> LDAny:
        """GET directory (schema) of available REST API data source

        ::
            :param url: REST API URL to the directory
            :type url: str

            :return: List of the Fortigate objects
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
        """Check does an object exists in the Fortigate.

        ::
            :param url: REST API URL to the object
            :type url: str

            :return: Session response
                *<Response [200]>* Object exist
                *<Response [404]>* Object does not exist
            :rtype: Response
        """
        return self._response("get", url)

    def get(self, url: str) -> LDAny:
        """GET object configured in the Fortigate.

        ::
            :param url: REST API URL to the object
            :type url: str

            :return: List of the Fortigate objects
            :rtype: List[dict]
        """
        response: Response = self._response("get", url)
        if not response.ok:
            logging.info("code=%s, reason=%s, url=%s", response.status_code, response.reason, url)
            return []
        response_json = response.json()
        results: LDAny = response_json.get("results") or []
        return results

    def post(self, url: str, data: DAny) -> Response:
        """POST (create) object in the Fortigate based on the data.

        ::
            :param url: REST API URL to the object
            :type url: str

            :param data: Data of the object
            :type data: dict

            :return: Session response
                *<Response [200]>* Object successfully created or already exists
                *<Response [500]>* Object already exist in the Fortigate
            :rtype: Response
        """
        response: Response = self._response("post", url, data)
        if not response.ok:
            self._logging(response)
        return response

    def put(self, url: str, data: DAny) -> Response:
        """PUT (update) existing object in the Fortigate.

        ::
            :param url: REST API URL to the object
            :type url: str

            :param data: Data of the object
            :type data: dict

            :return: Session response
                *<Response [200]>* Object successfully updated
                *<Response [404]>* Object has not been updated
            :rtype: Response
        """
        response: Response = self._response("put", url, data)
        if not response.ok:
            self._logging(response)
        return response

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
            raise TypeError(f"{session=} {Session} expected")
        return session

    def _logging(self, resp: Response) -> None:
        """Log response."""
        code = resp.status_code
        reason = resp.reason
        url = self._hide_secret(string=resp.url)
        msg = f"{code=} {reason=} {url=}"
        logging.info(msg)
        if logging.getLogger().level <= logging.DEBUG:
            logging.debug("text=%s", resp.text)

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

    def _response(self, method: Method, url: str, data: DAny = None) -> Response:
        """Call Session method and return Response.

        ::
            :param method: Session method: "delete", "get", "post", "put"
            :type method: str

            :param url: REST API URL to the object
            :type url: str

            :param data: Data of the object

            :return: Session response
            :rtype: Response
        """
        params: DAny = dict(
            url=self._valid_url(url),
            params=urlencode([("vdom", self.vdom)]),
            timeout=self.timeout,
            verify=self.verify,
        )
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
        """Add "https://" to `url` if absent."""
        if re.match("http(s)?://", url):
            return url
        url = url.strip("/")
        return f"{self.url}/{url}/"
