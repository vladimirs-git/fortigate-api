"""Application Object"""

from fortigate_api.base import Base


class Application(Base):
    """Application Object"""

    def __init__(self, fgt):
        super().__init__(fgt=fgt, url_obj="api/v2/cmdb/application/list/")
