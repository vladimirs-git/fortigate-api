"""Application Object."""

from fortigate_api.base import Base


class Application(Base):
    """Application Object.

    - Web UI: https://hostname/ng/utm/appctrl/sensor
    - API: https://hostname/api/v2/cmdb/application/list
    - Data: :ref:`Application.yml`
    """

    def __init__(self, rest):
        """Init Application Object.

        :param rest: :ref:`Fortigate` REST API connector.
        :type rest: Fortigate
        """
        super().__init__(rest=rest, url_obj="api/v2/cmdb/application/list/")
