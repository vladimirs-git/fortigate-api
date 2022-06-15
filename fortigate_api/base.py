"""Object Base"""

from operator import attrgetter

from fortigate_api import dict_, str_
from fortigate_api.types_ import DAny, LDAny, LStr, LResponse, StrInt
from requests import Response

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
    "api/v2/cmdb/system.snmp/community/",
    "api/v2/cmdb/system/interface/",
    "api/v2/cmdb/system/zone/",
)


class Base:
    """Object Base"""

    def __init__(self, fgt, url_obj: str, uid_key: str = "name"):
        """Object Base
        :param fgt: Fortigate connector
        :param url_obj: Part of REST API URL that pointing to object
        :param uid_key: Key of unique identifier
        """
        self.fgt = fgt
        self.url_ = f"{self.fgt.url}/{url_obj}"
        self.uid_key = uid_key

    def create(self, data: DAny) -> Response:
        """Creates fortigate-object in the Fortigate
        :param data: Data of the fortigate-object
        :return: Session response
            *<Response [200]>* Object successfully created or already exists
            *<Response [500]>* Object already exist in the Fortigate
        """
        dict_.check_mandatory(keys=["name"], **data)
        uid = dict_.get_quoted(key="name", **data)
        url = f"{self.url_}{uid}"
        exist = self.fgt.exist(url=url)
        if exist.ok:
            return exist
        return self.fgt.post(url=self.url_, data=data)

    # noinspection PyIncorrectDocstring
    def delete(self, **kwargs) -> Response:
        """Deletes the fortigate-object from Fortigate
        :param str uid: Identifier of the fortigate-object. Used to delete a single object
        :param list filter: Filters fortigate-objects by one or multiple conditions: equals "==",
            not equals "!=", contains "=@". Used to delete multiple objects
        :return: Session response
            *<Response [200]>* Object successfully deleted
            *<Response [404]>* Object absent in the Fortigate
        """
        dict_.check_only_one(["uid", "filter"], **kwargs)
        if uid := dict_.pop_str("uid", kwargs):
            uid = str_.quote(uid)
            url = f"{self.url_}{uid}"
            return self.fgt.delete(url=url)
        if "filter" in kwargs:
            return self._delete_by_filter(kwargs)
        raise KeyError(f"invalid {kwargs=}")

    def _delete_by_filter(self, kwargs):
        """Deletes the fortigate-objects from Fortigate by `filter`
        :param kwargs: Filters fortigate-objects by one or multiple conditions: equals "==",
            not equals "!=", contains "=@". Used to delete multiple objects
        :return: Session response with the highest status_code
        """
        responses: LResponse = []
        filters: LStr = dict_.pop_lstr(key="filter", data=kwargs)
        datas = self.get(filter=filters)
        for data in datas:
            uid = data[self.uid_key]
            url = f"{self.url_}{uid}"
            response = self.fgt.delete(url=url)
            responses.append(response)
        return self._highest_response(responses)

    # noinspection PyIncorrectDocstring
    def get(self, **kwargs) -> LDAny:
        """Gets fortigate-objects, all or filtered by some of params
        :param str uid: Filters fortigate-object by unique identifier. Used to get a single object
        :param list filter: Filters fortigate-objects by one or multiple conditions: equals "==",
            not equals "!=", contains "=@". Used to get multiple objects
        :return: *List[dict_]* List of the fortigate-objects
        """
        if kwargs:
            dict_.check_one_of(keys=["uid", "filter"], **kwargs)
        uid: str = dict_.pop_quoted(key="uid", data=kwargs)
        url = f"{self.url_}{uid}"
        url = str_.make_url(url, **kwargs)
        datas: LDAny = self.fgt.get(url)
        return datas

    def is_exist(self, uid: StrInt) -> bool:
        """Checks does a fortigate-object exists in the Fortigate
        :param uid: Identifier of the fortigate-object
        :return: True - object exist, False - object does not exist
        """
        if uid := str_.quote(uid):
            url = f"{self.url_}{uid}"
            response = self.fgt.exist(url=url)
            return response.ok
        raise ValueError(f"invalid {uid=}")

    def update(self, data: DAny, uid: StrInt = "") -> Response:
        """Updates address, address-group, etc. object, where `uid` is data["name"]
        :param data: Data of the fortigate-object
        :param uid: Name of the fortigate-object,
            taken from the `uid` parameter or from data["name"]
        :return: Session response
            *<Response [200]>* Object successfully updated
            *<Response [404]>* Object has not been updated
        """
        if not uid:
            uid = data.get("name") or ""
            if not uid:
                raise ValueError(f"absent {uid=} and data[\"name\"]")
        return self._update(data=data, uid=uid)

    # =========================== helpers ===========================

    @staticmethod
    def _highest_response(responses: LResponse) -> Response:
        """Return *Response* with the highest status_code, else returns *<Response [200]>*
        :param responses: List of Responses
        :return: Response with the highest status_code
        """
        if responses:
            responses = sorted(responses, key=attrgetter("status_code"))
            return responses[-1]
        response = Response()
        response.status_code = 200
        return response

    @staticmethod
    def _quote_url(url: str) -> str:
        """quote end of str_"""
        for known in IMPLEMENTED_OBJECTS:
            if url.startswith(known):
                end = url.replace(known, "", 1)
                return known + str_.quote(end)
        return url

    def _update(self, data: DAny, uid: StrInt) -> Response:
        """Updates fortigate-object in the Fortigate
        :param data: Data of the fortigate-object
        :param uid: Identifier of the fortigate-object
        :return: Session response
            *<Response [200]>* Object successfully updated
            *<Response [404]>* Object has not been updated
        """
        if uid := str_.quote(uid):
            url = f"{self.url_}{uid}"
            exist = self.fgt.exist(url=url)
            if not exist.ok:
                return exist
            return self.fgt.put(url=url, data=data)
        raise ValueError(f"invalid {uid=}")
