"""Antivirus Object."""

from fortigate_api.base import Base


class Antivirus(Base):
    """Antivirus Object."""

    def __init__(self, rest):
        """Antivirus Object.

        ::
            :param rest: Fortigate REST API connector
            :type rest: Fortigate
        """
        super().__init__(rest=rest, url_obj="api/v2/cmdb/antivirus/profile/")
