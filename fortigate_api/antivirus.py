"""Antivirus Object."""

from fortigate_api.base import Base


class Antivirus(Base):
    """Antivirus Object.

    - Web UI: https://hostname/ng/utm/antivirus/profile
    - API: https://hostname/api/v2/cmdb/antivirus/profile
    - Data: :ref:`Antivirus.yml`
    """

    def __init__(self, rest):
        """Antivirus Object.

        :param rest: :ref:`Fortigate` REST API connector.
        :type rest: Fortigate
        """
        super().__init__(rest=rest, url_obj="api/v2/cmdb/antivirus/profile/")
