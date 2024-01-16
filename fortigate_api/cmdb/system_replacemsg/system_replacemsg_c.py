"""Cmdb/system.replacemsg connectors."""

from fortigate_api.cmdb.system_replacemsg.admin import AdminSrC
from fortigate_api.cmdb.system_replacemsg.alertmail import AlertmailSrC
from fortigate_api.cmdb.system_replacemsg.auth import AuthSrC
from fortigate_api.cmdb.system_replacemsg.fortiguard_wf import FortiguardWfSrC
from fortigate_api.cmdb.system_replacemsg.ftp import FtpSrC
from fortigate_api.cmdb.system_replacemsg.http import HttpSrC
from fortigate_api.cmdb.system_replacemsg.icap import IcapSrC
from fortigate_api.cmdb.system_replacemsg.mail import MailSrC
from fortigate_api.cmdb.system_replacemsg.nac_quar import NacQuarSrC
from fortigate_api.cmdb.system_replacemsg.spam import SpamSrC
from fortigate_api.cmdb.system_replacemsg.sslvpn import SslvpnSrC
from fortigate_api.cmdb.system_replacemsg.traffic_quota import TrafficQuotaSrC
from fortigate_api.cmdb.system_replacemsg.utm import UtmSrC
from fortigate_api.cmdb.system_replacemsg.webproxy import WebproxySrC
from fortigate_api.fortigate import FortiGate


class SystemReplacemsgC:
    """Cmdb/system.replacemsg connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init SystemReplacemsgC."""

        self.admin = AdminSrC(fortigate, **kwargs)
        """:py:class:`.AdminSrC` cmdb/system.replacemsg/admin."""

        self.alertmail = AlertmailSrC(fortigate, **kwargs)
        """:py:class:`.AlertmailSrC` cmdb/system.replacemsg/alertmail."""

        self.auth = AuthSrC(fortigate, **kwargs)
        """:py:class:`.AuthSrC` cmdb/system.replacemsg/auth."""

        self.fortiguard_wf = FortiguardWfSrC(fortigate, **kwargs)
        """:py:class:`.FortiguardWfSrC` cmdb/system.replacemsg/fortiguard-wf."""

        self.ftp = FtpSrC(fortigate, **kwargs)
        """:py:class:`.FtpSrC` cmdb/system.replacemsg/ftp."""

        self.http = HttpSrC(fortigate, **kwargs)
        """:py:class:`.HttpSrC` cmdb/system.replacemsg/http."""

        self.icap = IcapSrC(fortigate, **kwargs)
        """:py:class:`.IcapSrC` cmdb/system.replacemsg/icap."""

        self.mail = MailSrC(fortigate, **kwargs)
        """:py:class:`.MailSrC` cmdb/system.replacemsg/mail."""

        self.nac_quar = NacQuarSrC(fortigate, **kwargs)
        """:py:class:`.NacQuarSrC` cmdb/system.replacemsg/nac-quar."""

        self.spam = SpamSrC(fortigate, **kwargs)
        """:py:class:`.SpamSrC` cmdb/system.replacemsg/spam."""

        self.sslvpn = SslvpnSrC(fortigate, **kwargs)
        """:py:class:`.SslvpnSrC` cmdb/system.replacemsg/sslvpn."""

        self.traffic_quota = TrafficQuotaSrC(fortigate, **kwargs)
        """:py:class:`.TrafficQuotaSrC` cmdb/system.replacemsg/traffic-quota."""

        self.utm = UtmSrC(fortigate, **kwargs)
        """:py:class:`.UtmSrC` cmdb/system.replacemsg/utm."""

        self.webproxy = WebproxySrC(fortigate, **kwargs)
        """:py:class:`.WebproxySrC` cmdb/system.replacemsg/webproxy."""
