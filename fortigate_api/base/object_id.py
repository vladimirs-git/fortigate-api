"""Object where key "id" is a unique identifier"""

from typing import List

from requests import Response

from fortigate_api import helper as h
from fortigate_api.base.object_base import ObjectBase
from fortigate_api.types_ import DAny, LDAny, StrInt, LStr


class ObjectID(ObjectBase):
    """Object where key "id" is a unique identifier"""

    def __init__(self, url_obj: str, fgt):
        """Object where key "id" is a unique identifier
        :param url_obj: Part of REST API URL that pointing to object
        :param fgt: Fortigate connector
        """
        super().__init__(fgt=fgt)
        self.url_obj = url_obj

    def create(self, data: DAny, **kwargs) -> Response:
        """Creates fortigate-object in the Fortigate
        :param data: Data of the fortigate-object
        :return: Session response. *<Response [200]>* Object successfully created,
            *<Response [500]>* Object already exist in the Fortigate
        """
        return self._create(url=self.url_obj, data=data)

    # noinspection PyShadowingBuiltins
    def delete(self, id: StrInt) -> Response:  # pylint: disable=redefined-builtin
        """Deletes fortigate-object from Fortigate
        :param id: Identifier of the fortigate-object
        :return: Session response. *<Response [200]>* Object successfully deleted,
            *<Response [404]>* Object absent in the Fortigate
        """
        id_ = h.int_(key="id", **{"id": id})
        url = f"{self.url_obj}{id_}"
        return self._delete(url=url)

    def delete_name(self, name: str) -> List[Response]:
        """Deletes fortigate-objects with the same name from Fortigate
        :param name: Name of the fortigate-objects
        :return: Session response. *List[Response]* - where
            *<Response [200]>* Object successfully deleted,
            *<Response [404]>* Object absent in the Fortigate
        """
        results: LDAny = self.get(name=name)
        ids = [str(d["id"]) for d in results]
        return self._delete_by_ids(ids)

    def _delete_by_ids(self, ids: LStr) -> List[Response]:
        """Deletes fortigate-objects from Fortigate by identifiers
        :param ids: Identifiers of the fortigate-objects
        :return: Session response. *<Response [200]>* Object successfully deleted,
            *<Response [404]>* Object absent in the Fortigate
        """
        responses: List[Response] = list()
        for id_ in ids:
            url = f"{self.url_obj}{id_}"
            responses.append(self._delete(url=url))
        return responses

    # noinspection PyIncorrectDocstring
    def get(self, **kwargs) -> LDAny:
        """Gets fortigate-objects, all or filtered by some of params.
        Need to use only one of params
        :param id: Filters fortigate-object by identifier
        :param name Filters fortigate-object by name
        :param filter: Filters fortigate-objects by one *str* or by multiple *List[str]*
            conditions: equal "==", not equal "!=", contain "=@"
        :return: *List[dict]* List of the fortigate-objects
        """
        self._name_to_filter(kwargs=kwargs)
        return self._get(url=self.url_obj, **kwargs)

    # noinspection PyShadowingBuiltins
    def is_exist(self, id: StrInt) -> bool:
        """Checks does a fortigate-object exists in the Fortigate
        :param id: Identifier of the fortigate-object
        :return: *bool* True - object exist, False - object does not exist
        """
        id_ = h.int_(key="id", **{"id": id})
        url = f"{self.url_obj}{id_}"
        return self._is_exist(url=url)

    def update(self, data: DAny) -> Response:
        """Updates fortigate-object in the Fortigate
        :param data: Data of the fortigate-object
        :return: Session response. *<Response [200]>* Object successfully updated,
            *<Response [404]>* Object has not been updated
        """
        id_ = str(data["id"])
        return self._update(id=id_, data=data)

    # noinspection PyShadowingBuiltins
    def _update(self, id: str, data: DAny) -> Response:
        """Updates fortigate-object in the Fortigate
        :param data: Data of the fortigate-object
        :return: Session response. *<Response [200]>* Object successfully updated,
            *<Response [404]>* Object has not been updated
        """
        url = f"{self.url}/{self.url_obj}{id}"
        exist = self.fgt.exist(url)
        if not exist.ok:
            return exist
        return self.fgt.put(url=url, data=data)
