"""Cmdb/firewall/policy connector."""
from requests import Response

from fortigate_api import helpers as h
from fortigate_api.connector import Connector
from fortigate_api.extended_filters import wrap_efilter
from fortigate_api.types_ import LDAny, StrInt, UStr


class PolicyFC(Connector):
    """Cmdb/firewall/policy connector."""

    uid = "policyid"
    _path = "api/v2/cmdb/firewall/policy"
    _path_ui = "ng/firewall/policy/policy/standard"

    # noinspection PyIncorrectDocstring
    @wrap_efilter
    def get(self, efilter: UStr = "", **kwargs) -> LDAny:  # pylint: disable=unused-argument
        """Get fortigate-policies, all or filtered by some of params.

        :param efilter: Filter fortigate-policies by one or multiple
            :ref:`Extended filtering conditions`.

        :param kwargs: Fortigate REST API parameters.
            ``filter`` - Filter fortigate-objects by one or multiple :ref:`Filtering conditions`.
            More details can be found at https://fndn.fortinet.net for related ``GET`` method.

        :return: List of the fortigate-policies.
        :rtype: List[dict]
        """
        return super().get(**kwargs)

    def move(self, policyid: StrInt, position: str, neighbor: StrInt) -> Response:
        """Move policy to before/after other neighbor-policy.

        :param policyid: Identifier of policy being moved.
        :type policyid: str or int

        :param position: "before" or "after" neighbor.
        :type position: str

        :param neighbor: Policy will be moved near to this neighbor-policy.
        :type neighbor: str or int

        :return: Session response.

            - `<Response [200]>` Policy successfully moved,
            - `<Response [500]>` Policy has not been moved.
        :rtype: Response
        """
        # if not self.fortigate.username:
        #     raise ValueError(f"Session based on username and password is required.")
        params = {
            "action": "move",
            # "username": self.fortigate.username,
            # "secretkey": self.fortigate.password,
            position: neighbor,
        }
        url = f"{self.url}/{policyid}"
        url = h.join_url_params(url, **params)
        return self.fortigate.put(url=url, data={})
