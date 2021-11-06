"""Universal Object"""

from __future__ import annotations

from requests import Response  # type: ignore

from fortigate_api.action import Action
from fortigate_api.typing_ import DAny, LDAny


class Object(Action):
    """Universal Object"""

    def create(self, data: DAny, **kwargs) -> Response:
        """Create new object on Fortigate
        :param kwargs: url - REST API URL to object
        :param data: data of object
        :return: session response"""
        url = kwargs["url"]
        return self._create(url=url, data=data)

    def delete(self, url: str) -> Response:
        """Delete object from Fortigate
        :param url: REST API URL to object
        :return: session response"""
        return self._delete(url=url)

    def get(self, **kwargs) -> LDAny:
        """Get objects data from Fortigate
        :param kwargs: params: url, name, id, filter, filters
        :return: data of objects"""
        return self._get(**kwargs)

    def update(self, data: DAny, **kwargs) -> Response:
        """Update existing object on Fortigate
        :param kwargs: url - REST API URL to object
        :param data: data of object
        :return: session response"""
        url = kwargs["url"]
        return self._update(url=url, data=data)
