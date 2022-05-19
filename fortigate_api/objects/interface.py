"""Interface Object"""

from fortigate_api.base.object_name import ObjectName
from fortigate_api.types_ import LDAny


class Interface(ObjectName):  # TODO unittest with vdom or example
    """Interface Object"""

    def __init__(self, fgt):
        super().__init__(url_obj="api/v2/cmdb/system/interface/", fgt=fgt)

    # noinspection PyIncorrectDocstring
    def get(self, **kwargs) -> LDAny:
        """Gets interface-objects in specified vdom, all or filtered by some of params
        :param name: Filters fortigate-object by unique identifier
        :param filter: Filters fortigate-objects by one *str* or by multiple *List[str]*
            conditions: equal "==", not equal "!=", contain "=@"
        :return: *List[dict]* List of interface-objects
        """
        interfaces: LDAny = self._get(url=self.url_obj, **kwargs)
        interfaces = [d for d in interfaces if d["vdom"] == self.fgt.vdom]
        return interfaces

    def get_all(self) -> LDAny:
        """Gets interface-objects, from all vdom"""
        return self._get(url=self.url_obj)
