"""Cmdb/certificate connectors."""

from fortigate_api.cmdb.certificate.ca import CaCC
from fortigate_api.cmdb.certificate.crl import CrlCC
from fortigate_api.cmdb.certificate.local import LocalCC
from fortigate_api.cmdb.certificate.remote import RemoteCC
from fortigate_api.fortigate import FortiGate


class CertificateC:
    """Cmdb/certificate connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init CertificateC."""
        self.ca = CaCC(fortigate, **kwargs)
        """:py:class:`.CaCC` cmdb/certificate/ca."""

        self.crl = CrlCC(fortigate, **kwargs)
        """:py:class:`.CrlCC` cmdb/certificate/crl."""

        self.local = LocalCC(fortigate, **kwargs)
        """:py:class:`.LocalCC` cmdb/certificate/local."""

        self.remote = RemoteCC(fortigate, **kwargs)
        """:py:class:`.RemoteCC` cmdb/certificate/remote."""
