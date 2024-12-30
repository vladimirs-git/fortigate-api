"""Cmdb/ssh-filter connectors."""

from fortigate_api.cmdb.ssh_filter.profile import ProfileSfC
from fortigate_api.fortigate import FortiGate


class SshFilterC:
    """Cmdb/ssh-filter connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init SshFilterC."""
        self.profile = ProfileSfC(fortigate, **kwargs)
        """:py:class:`.ProfileSfC` cmdb/ssh-filter/profile."""
