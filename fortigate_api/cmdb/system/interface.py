"""Cmdb/system/interface connector."""

from fortigate_api.connector import Connector
from fortigate_api.types_ import LDAny


class InterfaceSC(Connector):
    """Cmdb/system/interface connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/interface"
    _path_ui = "ng/interface"

    def get(self, all_vdoms: bool = False, **kwargs) -> LDAny:
        """Get interface-objects in specified vdom, all or filtered by some of params.

        :param bool all_vdoms: `True` - get interface-objects of all VDOMs,
            `False` - get interface-objects assigned to an initialized VDOM. Default is `False`.

        :param kwargs: Fortigate REST API parameters.
            ``filter`` - Filter fortigate-objects by one or multiple :ref:`Filtering conditions`.
            More details can be found at https://fndn.fortinet.net for related ``GET`` method.

        :return: List of the interface-objects.
        :rtype: List[dict]
        """
        items = super().get(**kwargs)
        if not all_vdoms:
            items = [d for d in items if d["vdom"] == self.fortigate.vdom]
        return items
