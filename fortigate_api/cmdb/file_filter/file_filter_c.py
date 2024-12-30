"""Cmdb/file-filter connectors."""

from fortigate_api.cmdb.file_filter.profile import ProfileFfC
from fortigate_api.fortigate import FortiGate


class FileFilterC:
    """Cmdb/file-filter connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init FileFilterC."""
        self.profile = ProfileFfC(fortigate, **kwargs)
        """:py:class:`.ProfileFfC` cmdb/file-filter/profile."""
