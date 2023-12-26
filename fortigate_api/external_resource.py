"""External Resource Object."""

from fortigate_api.base import Base


class ExternalResource(Base):
    """External Resource Object.

    - Web UI: https://hostname/ng/external-connector
    - API: https://hostname/api/v2/cmdb/system/external-resource
    - Data: :ref:`ExternalResource.yml`
    """

    def __init__(self, rest):
        """Init External Resource Object.

        :param rest: :ref:`Fortigate` REST API connector.
        :type rest: Fortigate
        """
        super().__init__(rest=rest, url_obj="api/v2/cmdb/system/external-resource/")
