"""FortiGate - Python wrapper for the FortiOS REST API."""

from __future__ import annotations

from requests import Response

from fortigate_api.fortigate_base import FortiGateBase
from fortigate_api.fortigate_base import HTTPS, TIMEOUT, VDOM
from fortigate_api.types_ import DAny, LDAny


class FortiGate(FortiGateBase):
    """FortiGate - Python wrapper for the FortiOS REST API."""

    # noinspection PyShadowingNames
    def __init__(  # pylint: disable=too-many-positional-arguments
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
        """Init FortiGate.

        :param str host: Fortigate hostname or ip address.

        :param str username: Administrator name. Mutually exclusive with `token`.

        :param str password: Administrator password. Mutually exclusive with `token`.

        :param str token: Token. Mutually exclusive with `username` and `password`.

        :param str scheme: Access method: `https` or `http`. Default is `https`.

        :param int port: TCP port. Default is `443` for scheme=`https`, `80` for scheme=`http`.

        :param int timeout: Session timeout (minutes). Default is 15.

        :param bool verify: Transport Layer Security.
            `True` - A trusted TLS certificate is required.
            `False` - Requests will accept any TLS certificate. Default is `False`.

        :param str vdom: Name of the virtual domain. Default is `root`.

        :param bool logging: Logging REST API response.
            `True` - Enable response logging, `False` - otherwise. Default is `False`.

        :param bool logging_error: Logging only the REST API response with error.
            `True` - Enable errors logging, `False` - otherwise. Default is `False`.
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
            "logging": logging,
            "logging_error": logging_error,
            **kwargs,
        }
        super().__init__(**kwargs)

    def login(self) -> None:  # pylint: disable=useless-parent-delegation
        """Login to the Fortigate using REST API and creates a Session object.

        - Validate `token` if object has been initialized with `token` parameter.
        - Validate `password` if object has been initialized with `username` parameter.

        :return: None. Creates Session object.
        """
        super().login()

    def logout(self) -> None:  # pylint: disable=useless-parent-delegation
        """Logout from the Fortigate using REST API, deletes Session object.

        - No need to log out if object has been initialized with `token` parameter.
        - Log out if object has been initialized with `username` parameter.

        :return: None. Deletes Session object
        """
        super().logout()

    def delete(self, url: str) -> Response:
        """DELETE the fortigate-object from the Fortigate.

        :param str url: REST API URL to the fortigate-object.

        :return: Session response.

            - `<Response [200]>` Object successfully deleted,
            - `<Response [400]>` Invalid URL,
            - `<Response [404]>` Object not found in the Fortigate.
        :rtype: Response
        """
        response: Response = self._response("delete", url)
        self._logging(response)
        return response

    def get(self, url: str) -> Response:
        """GET a Response object from the Fortigate.

        :param url url: REST API URL.

        :return: Response object.
        :rtype: Response
        """
        response: Response = self._response("get", url)
        self._logging(response)
        return response

    def get_result(self, url: str) -> DAny:
        """GET a single fortigate-object from the JSON results section.

        :param url url: REST API URL to the fortigate-objects.

        :return: dictionary of the fortigate-object.
        :rtype: dict
        """
        response: Response = self.get(url)
        if not response.ok:
            return {}
        data = response.json()
        return dict(data.get("results") or {})

    def get_results(self, url: str) -> LDAny:
        """GET list of fortigate-objects from the JSON results section.

        :param url url: REST API URL to the fortigate-objects.

        :return: List of the fortigate-objects.
        :rtype: List[dict]
        """
        response: Response = self._response("get", url)
        if not response.ok:
            return []
        data = response.json()
        return list(data.get("results") or [])

    def get_list(self, url: str) -> list:
        """GET list of items from the JSON root section.

        :param str url: REST API URL to the fortigate-objects.

        :return: List of the items.
        :rtype: List[dict]
        """
        response: Response = self._response("get", url)
        self._logging(response)
        if not response.ok:
            return []
        results: LDAny = list(response.json() or [])
        return results

    def post(self, url: str, data: DAny) -> Response:
        """POST (create) fortigate-object in the Fortigate based on the data.

        :param str url: REST API URL to the fortigate-object.

        :param dict data: Data of the fortigate-object.

        :return: Session response.

            - `<Response [200]>` Object successfully created,
            - `<Response [400]>` Invalid URL,
            - `<Response [500]>` Object already exist.
        :rtype: Response
        """
        response: Response = self._response("post", url, data)
        self._logging(response)
        return response

    def put(self, url: str, data: DAny) -> Response:
        """PUT (update) existing fortigate-object in the Fortigate.

        :param str url: REST API URL to the fortigate-object.

        :param dict data: Data of the fortigate-object.

        :return: Session response.

            - `<Response [200]>` Object successfully updated,
            - `<Response [400]>` Invalid URL,
            - `<Response [404]>` Object has not been updated.
        :rtype: Response
        """
        response: Response = self._response("put", url, data)
        self._logging(response)
        return response

    def directory(self, url: str) -> LDAny:
        """Get directory schema of available REST API data source.

        :param str url: REST API URL to the directory.

        :return: List of the fortigate-objects.
        :rtype: List[dict]
        """
        response: Response = self._response("get", url)
        self._logging(response)
        if not response.ok:
            return []
        response_json = response.json()
        results: LDAny = response_json.get("directory") or []
        return results

    def exist(self, url: str) -> Response:
        """Check if a fortigate-object exists in the Fortigate.

        :param str url: REST API URL to the fortigate-object.

        :return: Session response.

            - `<Response [200]>` Object exist,
            - `<Response [400]>` Invalid URL,
            - `<Response [404]>` Object does not exist.
        :rtype: Response
        """
        return self._response("get", url)
