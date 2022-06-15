"""**Fortigate** - Firewall Connector to login and logout.
Calls generic methods for working with objects: delete, get, post, put, exist.
"""
from __future__ import annotations

import json
import logging
import re
from typing import Iterable, Optional
from urllib.parse import urlencode

import requests
from fortigate_api import str_
from fortigate_api.types_ import DAny, LDAny
from requests import Session, Response
from requests.exceptions import SSLError  # type: ignore
from requests.packages import urllib3  # type: ignore

# noinspection PyUnresolvedReferences
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

PORT_80 = 80
PORT_443 = 443
HTTPS = "https"
TIMEOUT = 15
VDOM = "root"


class Fortigate:
    """**Fortigate** - Firewall Connector to login and logout.
    Calls generic methods for working with objects: delete, get, post, put, exist.
    """

    def __init__(self, host: str, username: str, password: str, **kwargs):
        """**Fortigate** - Firewall Connector
        :param host: Firewall ip address or hostname
        :param username: Administrator name
        :param password: Administrator password
        :param scheme: "https" or "http", by default "https"
        :param port: TCP port, by default 443 for "https", 80 for "http"
        :param timeout: Session timeout (minutes), by default 15
        :param vdom: Name of virtual domain, by default "root"
        """
        self.host = host
        self.username = username
        self.password = password
        self.scheme: str = self._init_scheme(**kwargs)
        self.port: int = self._init_port(**kwargs)
        self.timeout: int = int(kwargs.get("timeout") or TIMEOUT)
        self.vdom: str = str(kwargs.get("vdom") or VDOM)
        self._session: Optional[Session] = None

    def __repr__(self):
        host = self.host
        username = self.username
        password = "*" * len(self.password)
        scheme = self.scheme
        port = self.port if not (scheme == HTTPS and self.port == PORT_443) else ""
        timeout = self.timeout
        vdom = self.vdom
        params = [
            f"{host=!r}",
            f"{username=!r}",
            f"{password=!r}",
        ]
        params_optional = [
            f"{scheme=!r}" if scheme != HTTPS else "",
            f"{port=!r}" if port else "",
            f"{timeout=!r}" if timeout != TIMEOUT else "",
            f"{vdom=!r}" if vdom != VDOM else "",
        ]
        params.extend([s for s in params_optional if s])
        params_ = ", ".join([s for s in params if s])
        return f"{self.__class__.__name__}({params_})"

    # ============================= init =============================

    @staticmethod
    def _init_scheme(**kwargs) -> str:
        """Init scheme "https" or "http" """
        scheme = str(kwargs.get("scheme") or HTTPS)
        expected = ["https", "http"]
        if scheme not in expected:
            raise ValueError(f"{scheme=}, {expected=}")
        return scheme

    def _init_port(self, **kwargs) -> int:
        """Init port, 443 for "https", 80 for "http" """
        if port := int(kwargs.get("port") or 0):
            return port
        if self.scheme == "http":
            return PORT_80
        return PORT_443

    # =========================== property ===========================

    @property
    def is_connected(self) -> bool:
        """Check connection to Fortigate
        :return: True if session is connected to Fortigate"""
        if bool(self._session):
            return True
        return False

    @property
    def url(self):
        """Returns URL to Fortigate"""
        if self.port == 443:
            return f"{self.scheme}://{self.host}"
        return f"{self.scheme}://{self.host}:{self.port}"

    # =========================== methods ============================

    def delete(self, url: str) -> Response:
        """DELETE object from Fortigate
        :param url: REST API URL to the object
        :return: Session response
            *<Response [200]>* Object successfully deleted
            *<Response [404]>* Object absent in the Fortigate
        """
        url = self._valid_url(url)
        session: Session = self._get_session()
        try:
            response: Response = session.delete(url=url,
                                                params=urlencode([("vdom", self.vdom)]),
                                                timeout=self.timeout,
                                                verify=False)
        except Exception as ex:
            raise self._hide_secret_ex(ex)
        if not response.ok:
            self._logging(response)
        return response

    def exist(self, url: str) -> Response:
        """Checks does an object exists in the Fortigate
        :param url: REST API URL to the object
        :return: Session response
            *<Response [200]>* Object exist
            *<Response [404]>* Object does not exist
        """
        url = self._valid_url(url)
        session: Session = self._get_session()
        response: Response = session.get(url=url,
                                         params=urlencode([("vdom", self.vdom)]),
                                         timeout=self.timeout,
                                         verify=False)
        return response

    def get(self, url: str) -> LDAny:
        """GET object configured in the Fortigate
        :param url: REST API URL to the object
        :return: *List[dict_]* of the objects data
        """
        url = self._valid_url(url)
        session: Session = self._get_session()
        try:
            response: Response = session.get(url=url,
                                             params=urlencode([("vdom", self.vdom)]),
                                             timeout=self.timeout,
                                             verify=False)
        except Exception as ex:
            raise self._hide_secret_ex(ex)
        if not response.ok:
            logging.info("code=%s, reason=%s, str_=%s", response.status_code, response.reason, url)
            return []
        result: LDAny = response.json()["results"]
        return result

    def login(self) -> Fortigate:
        """Login to Fortigate. Save logged-in session to self._session
        :return: self *Fortigate* object
        """
        session: Session = requests.session()
        try:
            session.post(url=f"{self.url}/logincheck",
                         data=urlencode([("username", self.username),
                                         ("secretkey", self.password)]),
                         timeout=self.timeout,
                         verify=False)
        except Exception as ex:
            raise self._hide_secret_ex(ex)
        for cookie in session.cookies:
            if cookie.name == "ccsrftoken" and isinstance(cookie.value, str):
                session.headers.update({"X-CSRFTOKEN": cookie.value[1:-1]})
                break
        else:
            raise ValueError("invalid login credentials, absent cookie ccsrftoken")
        response: Response = session.get(url=f"{self.url}/api/v2/cmdb/system/vdom")
        response.raise_for_status()
        self._session = session
        return self

    def logout(self) -> None:
        """Logout Fortigate. Delete logged-in session"""
        if self._session:
            try:
                self._session.get(url=f"{self.url}/logout", timeout=self.timeout, verify=False)
            except SSLError:
                pass
            self._session = None

    def post(self, url: str, data: DAny) -> Response:
        """POST (create) object in the Fortigate based on the data
        :param url: REST API URL to the object
        :param data: Data of the object
        :return: Session response
            *<Response [200]>* Object successfully created or already exists
            *<Response [500]>* Object already exist in the Fortigate
        """
        url = self._valid_url(url)
        session: Session = self._get_session()
        try:
            response: Response = session.post(url=url,
                                              params=urlencode([("vdom", self.vdom)]),
                                              data=json.dumps(data),
                                              timeout=self.timeout,
                                              verify=False)
        except Exception as ex:
            raise self._hide_secret_ex(ex)
        if not response.ok:
            self._logging(response)
        return response

    def put(self, url: str, data: DAny) -> Response:
        """PUT (update) existing object in the Fortigate
        :param url: REST API URL to the object
        :param data: Data of the object
        :return: Session response
            *<Response [200]>* Object successfully updated
            *<Response [404]>* Object has not been updated
        """
        url = self._valid_url(url)
        session: Session = self._get_session()
        try:
            response: Response = session.put(url=url,
                                             params=urlencode([("vdom", self.vdom)]),
                                             data=json.dumps(data),
                                             timeout=self.timeout,
                                             verify=False)
        except Exception as ex:
            raise self._hide_secret_ex(ex)
        if not response.ok:
            self._logging(response)
        return response

    # =========================== helpers ============================

    def _get_session(self) -> Session:
        """Returns an existing session or create a new one"""
        if not self._session:
            self.login()
        if isinstance(self._session, Session):
            return self._session
        raise ValueError(f"absent session={self._session}")

    def _logging(self, resp: Response) -> None:
        """Logging response"""
        code = resp.status_code
        reason = resp.reason
        url = self._hide_secret(string=resp.url)
        msg = f"{code=} {reason=} {url=}"
        logging.info(msg)
        if logging.getLogger().level <= logging.DEBUG:
            logging.debug("text=%s", resp.text)

    def _hide_secret(self, string: str) -> str:
        """Hides password, secretkey in text (for safe logging)"""
        if not self.password:
            return string
        result = string.replace(self.password, "<hidden>")
        quoted_password = str_.quote(self.password)
        result = result.replace(quoted_password, "<hidden>")
        return result

    def _hide_secret_ex(self, ex):
        """Hides secretkey in exception (for safe logging)"""
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

    def _valid_url(self, url: str) -> str:
        """Adds "https://" to `url`"""
        if re.match("http(s)?://", url):
            return url
        url = url.strip("/")
        return f"{self.url}/{url}/"
