"""Application Object."""

from fortigate_api.base import Base


class Application(Base):
    """Application Object."""

    def __init__(self, rest):
        """Application Object.

        ::
            :param rest: Fortigate REST API connector
            :type rest: Fortigate
        """
        super().__init__(rest=rest, url_obj="api/v2/cmdb/application/list/")
