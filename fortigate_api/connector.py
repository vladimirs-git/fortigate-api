"""Connector, a set of methods to modify objects in the Fortigate."""

from requests import Response
from vhelpers import vdict, vlist

from fortigate_api import helpers as h
from fortigate_api.fortigate import FortiGate
from fortigate_api.types_ import DAny, LDAny, LResponse, StrInt, UStr


class Connector:
    """Connector, a set of methods used to modify objects in the Fortigate."""

    uid: str = "name"
    """Unique identifier of fortigate-object."""

    _path: str = ""
    """Part of the REST API URL that points to the fortigate-object."""

    _path_ui: str = ""
    """Part of the web user interface URL that points to the fortigate-object."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init Connector.

        :param fortigate: Fortigate REST API connector.
        """
        _ = kwargs  # noqa
        self.fortigate = fortigate

    @property
    def url(self) -> str:
        """URL to the fortigate-object."""
        return f"{self.fortigate.url}/{self._path}"

    def create(self, data: DAny) -> Response:
        """Create the fortigate-object in the Fortigate.

        :param dict data: Data of the fortigate-object.
            More details can be found at https://fndn.fortinet.net for related ``POST`` method.

        :return: Session response.

            - `<Response [200]>` Object successfully created,
            - `<Response [500]>` Object already exists.
        :rtype: Response
        """
        return self.fortigate.post(url=self.url, data=data)

    # noinspection PyShadowingBuiltins
    def delete(
        self,
        uid: StrInt = "",
        filter: UStr = "",  # pylint: disable=redefined-builtin
        **kwargs,
    ) -> Response:
        """Delete the fortigate-object from the Fortigate.

        :param uid: Identifier of the fortigate-object.
            Used to delete a single object.
        :type uid: str or int

        :param filter: Filter fortigate-objects by one or multiple :ref:`Filtering conditions`.
            Used to delete multiple objects.
        :type filter: str or List[str]

        :param kwargs: Fortigate REST API parameters.
            More details can be found at https://fndn.fortinet.net for related ``DELETE`` method.

        :return: Session response.

            - `<Response [200]>` Object successfully deleted,
            - `<Response [404]>` Object not found in the Fortigate.
        :rtype: Response
        """
        if not uid:
            uid = str(kwargs.get(self.uid) or "")
        h.check_uid_filter(uid, filter)
        if filter:
            return self._delete_by_filter(filter)
        uid = h.quote(uid)
        url = f"{self.url}/{uid}"
        return self.fortigate.delete(url=url)

    def get(self, **kwargs) -> LDAny:
        """Get fortigate-objects, all or filtered by some parameters.

        :param kwargs: Fortigate REST API parameters.
            ``filter`` - Filter fortigate-objects by one or multiple :ref:`Filtering conditions`.
            More details can be found at https://fndn.fortinet.net for related ``GET`` method.

        :return: List of the fortigate-objects.
        :rtype: List[dict]
        """
        uid = h.quote(vdict.pop(kwargs, key=self.uid))
        url = f"{self.url}/{uid}".rstrip("/")
        url = h.join_url_params(url=url, **kwargs)
        if self.uid:
            items: LDAny = self.fortigate.get_results(url)
        else:
            item: DAny = self.fortigate.get_result(url)
            items = [item]
        return items

    def is_exist(self, uid: StrInt) -> bool:
        """Check if a fortigate-object exists in the Fortigate.

        :param uid: Identifier of the fortigate-object.
        :type uid: str or int

        :return: True - object exists, False - object does not exist.
        :rtype: bool
        """
        uid = h.quote(uid)
        if not uid:
            raise ValueError("uid is required.")
        url = f"{self.url}/{uid}"
        response = self.fortigate.exist(url)
        return response.ok

    def update(self, data: DAny) -> Response:
        """Update fortigate-object on the Fortigate.

        :param dict data: Data of the fortigate-object to update.
            More details can be found at https://fndn.fortinet.net for related ``PUT`` method.

        :return: Session response.

            - `<Response [200]>` Object successfully updated,
            - `<Response [404]>` Object has not been updated.
        :rtype: Response
        """
        uid: str = self._get_uid(data)
        url = f"{self.url}/{uid}".rstrip("/")
        return self.fortigate.put(url=url, data=data)

    # noinspection PyShadowingBuiltins
    def _delete_by_filter(self, filter: UStr) -> Response:  # pylint: disable=redefined-builtin
        """Delete the fortigate-objects from the Fortigate by `filter`.

        :param filter: Filter fortigate-objects by one or multiple :ref:`Filtering conditions`.
            Used to delete multiple objects.
        :type filter: str or List[str]

        :return: Session response with the highest (worst) status_code.

            - `<Response [200]>` Object successfully deleted,
            - `<Response [404]>` Object not found in the Fortigate.
        :rtype: Response
        """
        responses: LResponse = []
        filters = vlist.to_list(filter)
        items: LDAny = self.get(filter=filters)
        for data in items:
            uid = h.quote(data[self.uid])
            url = f"{self.url}/{uid}"
            response = self.fortigate.delete(url=url)
            responses.append(response)
        return h.highest_response(responses)

    def _get_uid(self, data) -> str:
        """Get UID value based on the UID key.

        :param data: A dictionary containing the UID value.
        :return: The UID value extracted from the data.
        :raises ValueError: If the UID is required but not present in the data.
        """
        if not self.uid:
            return ""
        if self.uid not in data:
            raise ValueError(f"{self.uid} value is required.")
        uid = str(data[self.uid])
        uid = h.quote(uid)
        return uid
