"""Object where key "name" is a unique identifier"""

from requests import Response  # type: ignore

from fortigate_api import helper as h
from fortigate_api.base.object_base import ObjectBase
from fortigate_api.types_ import DAny, LDAny


class ObjectName(ObjectBase):
    """Object where key "name" is a unique identifier"""

    def __init__(self, url_obj: str, fgt):
        """Object where key "name" is a unique identifier
        :param url_obj: Part of REST API URL that pointing to fortigate-object
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

    def delete(self, name: str) -> Response:
        """Deletes the fortigate-object from Fortigate
        :param name: Unique identifier of the fortigate-object
        :return: Session response. *<Response [200]>* Object successfully deleted,
            *<Response [404]>* Object absent in the Fortigate
        """
        name = h.quote_(name)
        url = f"{self.url_obj}{name}"
        return self._delete(url=url)

    # noinspection PyIncorrectDocstring
    def get(self, **kwargs) -> LDAny:
        """Gets fortigate-objects, all or filtered by some of params.
        Need to use only one of params
        :param name: Filters fortigate-object by unique identifier
        :param filter: Filters fortigate-objects by one *str* or by multiple *List[str]*
            conditions: equal "==", not equal "!=", contain "=@"
        :return: *List[dict]* List of the fortigate-objects
        """
        return self._get(url=self.url_obj, **kwargs)

    def is_exist(self, name: str) -> bool:
        """Checks does a fortigate-object exists in the Fortigate
        :param name: Unique identifier of the fortigate-object
        :return: *bool* True - object exist, False - object does not exist
        """
        url = f"{self.url_obj}{h.quote_(name)}"
        return self._is_exist(url=url)

    def update(self, data: DAny) -> Response:
        """Updates fortigate-object in the Fortigate
        :param data: Data of the fortigate-object
        :return: Session response. *<Response [200]>* Object successfully updated,
            *<Response [404]>* Object has not been updated
        """
        return self._update(url=self.url_obj, data=data)
