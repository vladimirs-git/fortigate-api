"""Interface Object"""

from fortigate_api.base import Base
from fortigate_api import dict_
from fortigate_api.types_ import LDAny


class Interface(Base):
    """Interface Object"""

    def __init__(self, fgt):
        super().__init__(fgt=fgt, url_obj="api/v2/cmdb/system/interface/")

    # noinspection PyIncorrectDocstring
    def get(self, **kwargs) -> LDAny:
        """Gets interface-objects in specified vdom, all or filtered by some of params
        :param str uid: Filters interface-object by unique identifier. Used to get a single object
        :param list filter: Filters interface-objects by one or multiple conditions: equals "==",
            not equals "!=", contains "=@". Used to get multiple objects
        :param bool all: Gets all interface-objects from all vdom
        :return: *List[dict_]* List of interface-objects
        """
        if kwargs.get("all"):
            dict_.pop_quoted(key="all", data=kwargs)
            return super().get(**kwargs)
        interfaces = super().get(**kwargs)
        interfaces = [d for d in interfaces if d["vdom"] == self.fgt.vdom]
        return interfaces
