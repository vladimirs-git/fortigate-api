"""Cmdb/system.snmp connectors."""

from fortigate_api.cmdb.system_snmp.community import CommunitySsC
from fortigate_api.cmdb.system_snmp.sysinfo import SysinfoSsC
from fortigate_api.cmdb.system_snmp.user import UserSsC
from fortigate_api.fortigate import FortiGate


class SystemSnmpC:
    """Cmdb/system.snmp connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init SystemSnmpC."""
        self.community = CommunitySsC(fortigate, **kwargs)
        """:py:class:`.CommunitySsC` cmdb/system.snmp/community."""

        self.sysinfo = SysinfoSsC(fortigate, **kwargs)
        """:py:class:`.SysinfoSsC` cmdb/system.snmp/sysinfo."""

        self.user = UserSsC(fortigate, **kwargs)
        """:py:class:`.UserSsC` cmdb/system.snmp/user."""
