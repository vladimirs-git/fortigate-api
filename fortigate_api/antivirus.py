"""Antivirus Object."""

from fortigate_api.base import Base


class Antivirus(Base):
    """Antivirus Object."""

    def __init__(self, fgt):
        """Antivirus Object.

        ::
            :param fgt: Fortigate connector
            :type fgt: Fortigate
        """
        super().__init__(fgt=fgt, url_obj="api/v2/cmdb/antivirus/profile/")
