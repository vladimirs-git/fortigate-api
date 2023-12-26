"""Parent of FortigateAPI objects: Address, AddressGroup, Policy, etc."""

from operator import attrgetter

from requests import Response

from fortigate_api import helpers as h
from fortigate_api.types_ import DAny, LDAny, LStr, LResponse, StrInt

IMPLEMENTED_OBJECTS = (
    "api/v2/cmdb/antivirus/profile/",
    "api/v2/cmdb/application/list/",
    "api/v2/cmdb/firewall.schedule/onetime/",
    "api/v2/cmdb/firewall.service/category/",
    "api/v2/cmdb/firewall.service/custom/",
    "api/v2/cmdb/firewall.service/group/",
    "api/v2/cmdb/firewall/address/",
    "api/v2/cmdb/firewall/addrgrp/",
    "api/v2/cmdb/firewall/internet-service/",
    "api/v2/cmdb/firewall/ippool/",
    "api/v2/cmdb/firewall/policy/",
    "api/v2/cmdb/firewall/vip/",
    "api/v2/cmdb/system.dhcp/server/",
    "api/v2/cmdb/system.snmp/community/",
    "api/v2/cmdb/system/external-resource/",
    "api/v2/cmdb/system/interface/",
    "api/v2/cmdb/system/vdom/",
    "api/v2/cmdb/system/zone/",
    "api/v2/cmdb/system/vdom",
)


class Base:
    """Connector, a set of methods to modify objects in the Fortigate."""

    def __init__(self, rest, url_obj: str, uid_key: str = "name"):
        """Init Connector.

        :param Fortigate rest: :ref:`Fortigate` REST API connector.

        :param str url_obj: Part of REST API URL that pointing to object.

        :param str uid_key: Key of unique identifier: `name`, `id`, `policyid`.
            Default in `name`.
        """
        self.rest = rest
        self.url_ = f"{self.rest.url}/{url_obj}"
        self.uid_key = uid_key

    def create(self, data: DAny) -> Response:
        """Create the fortigate-object in the Fortigate.

        :param dict data: Data of the fortigate-object.

        :return: Session response.

            - `<Response [200]>` Object successfully created or already exists,
            - `<Response [400]>` Invalid URL,
            - `<Response [500]>` Object already exist.
        :rtype: requests.Response
        """
        h.check_mandatory(keys=["name"], **data)
        return self.rest.post(url=self.url_, data=data)

    # noinspection PyIncorrectDocstring
    def delete(self, uid: StrInt = "", **kwargs) -> Response:
        """Delete the fortigate-object from the Fortigate.

        :param uid: Identifier of the fortigate-object.
            Used to delete a single object.
        :type uid: str or int

        :param filter: Filter fortigate-objects by one or multiple :ref:`filtering conditions`.
            Used to delete multiple objects.
            If no objects have been found, return <Response [404]>.
        :type filter: str or List[str]

        :return: Session response.

            - `<Response [200]>` Object successfully deleted,
            - `<Response [400]>` Invalid URL,
            - `<Response [404]>` Object not found in the Fortigate.
        :rtype: requests.Response
        """
        if uid:
            kwargs["uid"] = uid
        h.check_only_one(["uid", "filter"], **kwargs)
        if uid := h.pop_str("uid", kwargs):
            uid = h.quote(uid)
            url = f"{self.url_}{uid}"
            return self.rest.delete(url=url)
        if "filter" in kwargs:
            return self._delete_by_filter(kwargs)
        raise ValueError(f"Invalid {uid=} {kwargs=}.")

    # noinspection PyIncorrectDocstring
    def get(self, **kwargs) -> LDAny:
        """Get fortigate-objects, all or filtered by some parameters.

        :param uid: Filter fortigate-object by unique identifier.
            Used to get a single object.
        :type uid: str or int

        :param filter: Filter fortigate-objects by one or multiple :ref:`filtering conditions`. 
            Used to get multiple objects.
        :type filter: str or List[str]

        :return: List of the fortigate-objects.
        :rtype: List[dict]
        """
        if kwargs:
            h.check_one_of(keys=["uid", "filter"], **kwargs)
        uid: str = h.pop_quoted(key="uid", data=kwargs)
        url = f"{self.url_}{uid}"
        url = h.make_url(url, **kwargs)
        datas: LDAny = self.rest.get(url)
        return datas

    def update(self, data: DAny, uid: StrInt = "") -> Response:
        """Update fortigate-object where ``uid`` is ``data["name"]``.

        :param dict data: Data of the fortigate-object.

        :param uid: Name of the fortigate-object,
            taken from the ``uid`` parameter or from ``data["name"]``.
        :type uid: str or int

        :return: Session response.

            - `<Response [200]>` Object successfully updated,
            - `<Response [400]>` Invalid URL,
            - `<Response [404]>` Object has not been updated.
        :rtype: requests.Response
        """
        if not uid:
            uid = data.get("name") or ""
            if not uid:
                raise ValueError(f"Absent {uid=} and data[\"name\"].")
        return self._update(data=data, uid=uid)

    def is_exist(self, uid: StrInt) -> bool:
        """Check if a fortigate-object exists in the Fortigate.

        :param uid: Identifier of the fortigate-object.
        :type uid: str or int

        :return: True - object exist, False - object does not exist.
        :rtype: bool
        """
        if uid := h.quote(uid):
            url = f"{self.url_}{uid}"
            response = self.rest.exist(url=url)
            return response.ok
        raise ValueError(f"Invalid {uid=}.")

    # =========================== helpers ===========================

    def _delete_by_filter(self, kwargs) -> Response:
        """Delete the fortigate-objects from the Fortigate by `filter`.

        :param kwargs: Filter fortigate-objects by one or multiple :ref:`filtering conditions`.
            Used to delete multiple objects.

        :return: Session response with the highest (worst) status_code.

            - `<Response [200]>` Object successfully deleted,
            - `<Response [400]>` Invalid URL,
            - `<Response [404]>` Object not found in the Fortigate.
        :rtype: requests.Response
        """
        responses: LResponse = []
        filters: LStr = h.pop_lstr(key="filter", data=kwargs)
        datas = self.get(filter=filters)
        for data in datas:
            uid = h.quote(data[self.uid_key])
            url = f"{self.url_}{uid}"
            response = self.rest.delete(url=url)
            responses.append(response)
        return self._highest_response(responses)

    @staticmethod
    def _highest_response(responses: LResponse) -> Response:
        """Return Response object with the highest status_code

        If no objects have been found, return <Response [404]>.

        :param responses: List of Response objects.
        :type responses: List[Response]

        :return: Response with the highest (worst) status_code or <Response [404]>.
        :rtype: requests.Response
        """
        if responses:
            responses = sorted(responses, key=attrgetter("status_code"))
            return responses[-1]
        response = Response()
        response.status_code = 404
        return response

    @staticmethod
    def _quote_url(url: str) -> str:
        """Quote end of url."""
        for known in IMPLEMENTED_OBJECTS:
            if url.startswith(known):
                end = url.replace(known, "", 1)
                return known + h.quote(end)
        return url

    def _update(self, data: DAny, uid: StrInt) -> Response:
        """Update fortigate-object in the Fortigate.

        :param dict data: Data of the fortigate-object.

        :param uid: Identifier of the fortigate-object.
        :type uid: str or int

        :return: Session response.

            - `<Response [200]>` Object successfully updated,
            - `<Response [400]>` Invalid URL,
            - `<Response [404]>` Object has not been updated.
        :rtype: requests.Response
        """
        uid = h.quote(uid)
        if not uid:
            raise ValueError("uid is required.")
        url = f"{self.url_}{uid}"
        return self.rest.put(url=url, data=data)
