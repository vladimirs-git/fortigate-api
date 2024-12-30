"""Cmdb/credential-store connectors."""

from fortigate_api.cmdb.credential_store.domain_controller import DomainControllerCsC
from fortigate_api.fortigate import FortiGate


class CredentialStoreC:
    """Cmdb/credential-store connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init CredentialStoreC."""
        self.domain_controller = DomainControllerCsC(fortigate, **kwargs)
        """:py:class:`.DomainControllerCsC` cmdb/credential-store/domain-controller."""
