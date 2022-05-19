"""DEVELOPING (NOT FINISHED)
**Object** - creates, deletes, gets, updates any objects in the Fortigate.
You must be familiar with the REST API URL to interested object.
"""

from requests import Response  # type: ignore

from fortigate_api.base.object_base import ObjectBase
from fortigate_api.types_ import DAny, LDAny


# noinspection PyIncorrectDocstring
class Object(ObjectBase):
    """**Object** - creates, deletes, gets, updates any objects in the Fortigate"""

    def create(self, data: DAny, **kwargs) -> Response:
        """Creates new object in the Fortigate
        :param url: REST API URL to the object
        :param data: Data of the object
        :return: Session response. *<Response [200]>* Object successfully created,
            *<Response [500]>* Object already exist in the Fortigate
        """
        url = kwargs["url"]
        return self._create(url=url, data=data)

    def delete(self, url: str) -> Response:
        """Deletes object from Fortigate
        :param url: REST API URL to the object
        :return: Session response. *<Response [200]>* Object successfully deleted,
            *<Response [404]>* Object absent in the Fortigate
        """
        return self._delete(url=url)

    def get(self, **kwargs) -> LDAny:
        """Gets objects data from Fortigate
        :param url: REST API URL to the object
        :param filter: Key and value of filter
        :return: Data of the objects
        """
        return self._get(**kwargs)

    def update(self, data: DAny, **kwargs) -> Response:
        """Updates existing object in the Fortigate
        :param url: REST API URL to the object
        :param data: Data of the object
        :return: Session response. *<Response [200]>* Object successfully updated,
            *<Response [404]>* Object has not been updated
        """
        url = kwargs["url"]
        return self._update(url=url, data=data)

    def is_exist(self, url: str) -> bool:
        """Checks does an object exists in the Fortigate
        :param url: REST API URL to the object
        :return: True - object exist, False - object does not exist
        """
        return self._is_exist(url=url)
