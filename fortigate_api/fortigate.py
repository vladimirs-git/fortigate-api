"""Fortigate Connector"""

import json
import logging
from typing import Iterable, Optional
from urllib.parse import urlencode

import requests  # type: ignore
from requests import Session, Response
from requests.exceptions import SSLError  # type: ignore
from requests.packages import urllib3  # type: ignore

from fortigate_api import helper
from fortigate_api.typing_ import DAny, LDAny

# noinspection PyUnresolvedReferences
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Fortigate:
    """Fortigate Connector"""

    def __init__(self, host: str, username: str, password: str, **kwargs):
        self.host = host
        self.username = username
        self.password = password
        self.port = self._port(**kwargs)
        self.timeout = self._timeout(**kwargs)
        self.vdom = self._vdom(**kwargs)
        self._session: Optional[Session] = None

    def __repr__(self):
        return f"{self.url} vdom={self.vdom}"

    # ============================= init =============================

    @staticmethod
    def _port(**kwargs) -> int:
        """Return tcp port for API URL"""
        return helper.int_(key="port", **kwargs) or 443

    @staticmethod
    def _timeout(**kwargs) -> int:
        """Return session timeout (minutes)"""
        return helper.int_(key="timeout", **kwargs) or 15

    @staticmethod
    def _vdom(**kwargs) -> str:
        """Return name of virtual domain"""
        return helper.str_(key="vdom", **kwargs) or "root"

    # ======================= generic methods ========================

    @property
    def url(self):
        """Return URL to API"""
        if self.port == 443:
            return f"https://{self.host}"
        return f"https://{self.host}:{self.port}"

    def login(self) -> Session:
        """Login to Fortigate"""
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
        return session

    def logout(self) -> None:
        """Logout Fortigate"""
        if self._session:
            try:
                self._session.get(url=f"{self.url}/logout", timeout=self.timeout, verify=False)
            except SSLError:
                pass
            self._session = None

    def delete(self, url: str) -> Response:
        """DELETE object from Fortigate
        :param url: REST API URL to object
        :return: session response"""
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

    def get(self, url: str) -> LDAny:
        """GET object configured on Fortigate
        :param url: REST API URL to object
        :return: return list of objects data"""
        session: Session = self._get_session()
        try:
            response: Response = session.get(url=url,
                                             params=urlencode([("vdom", self.vdom)]),
                                             timeout=self.timeout,
                                             verify=False)
        except Exception as ex:
            raise self._hide_secret_ex(ex)
        if not response.ok:
            logging.info("code=%s, reason=%s, url=%s", response.status_code, response.reason, url)
            return list()
        result: LDAny = response.json()["results"]
        return result

    def post(self, url: str, data: DAny) -> Response:
        """POST (create) object on Fortigate based on data
        :param url: REST API URL to object
        :param data: data of new object
        :return: session response"""
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
        """PUT (update) existing object on Fortigate
        :param url: REST API URL to object
        :param data: data of object
        :return: session response"""
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

    def exist(self, url: str) -> Response:
        """Check does object exists on Fortigate
        :param url: REST API URL to object
        :return: session response, if object exist status_code==200"""
        session: Session = self._get_session()
        response: Response = session.get(url=url,
                                         params=urlencode([("vdom", self.vdom)]),
                                         timeout=self.timeout,
                                         verify=False)
        return response

    # =========================== helpers ============================

    def _get_session(self) -> Session:
        """return an existing session or create a new one"""
        return self._session if self._session else self.login()

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
        """hide password, secretkey in text (for safe logging)"""
        if not self.password:
            return string
        result = string.replace(self.password, "<hidden>")
        quoted_password = helper.quote(self.password)
        result = result.replace(quoted_password, "<hidden>")
        return result

    def _hide_secret_ex(self, ex):
        """hide secretkey in exception (for safe logging)"""
        if hasattr(ex, "args"):
            if (args := getattr(ex, "args")) and isinstance(args, Iterable):
                msgs = list()  # result
                for arg in args:
                    if isinstance(arg, str):
                        msgs.append(self._hide_secret(string=arg))
                    else:
                        msgs.append(arg)
                return type(ex)(tuple(msgs))
        return ex
