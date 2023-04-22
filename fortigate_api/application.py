"""Application Object."""

from fortigate_api.base import Base


class Application(Base):
    """Application Object."""

    def __init__(self, fgt):
        """Application Object.

        ::
            :param fgt: Fortigate connector
            :type fgt: Fortigate
        """
        super().__init__(fgt=fgt, url_obj="api/v2/cmdb/application/list/")
