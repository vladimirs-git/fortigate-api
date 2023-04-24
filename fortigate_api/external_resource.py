"""External Resource Object."""

from fortigate_api.base import Base


class ExternalResource(Base):
    """External Resource Object."""

    def __init__(self, rest):
        """External Resource Object.

        ::
            :param rest: Fortigate REST API connector
            :type rest: Fortigate
        """
        super().__init__(rest=rest, url_obj="api/v2/cmdb/system/external-resource/")
