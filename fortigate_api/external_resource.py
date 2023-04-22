"""External Resource Object."""

from fortigate_api.base import Base


class ExternalResource(Base):
    """External Resource Object."""

    def __init__(self, fgt):
        """External Resource Object.

        ::
            :param fgt: Fortigate connector
            :type fgt: Fortigate
        """
        super().__init__(fgt=fgt, url_obj="api/v2/cmdb/system/external-resource/")
