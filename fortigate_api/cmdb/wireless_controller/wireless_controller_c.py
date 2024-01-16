"""Cmdb/wireless-controller connectors."""

from fortigate_api.cmdb.wireless_controller.access_control_list import AccessControlListWcC
from fortigate_api.cmdb.wireless_controller.address import AddressWcC
from fortigate_api.cmdb.wireless_controller.addrgrp import AddrgrpWcC
from fortigate_api.cmdb.wireless_controller.ap_status import ApStatusWcC
from fortigate_api.cmdb.wireless_controller.apcfg_profile import ApcfgProfileWcC
from fortigate_api.cmdb.wireless_controller.arrp_profile import ArrpProfileWcC
from fortigate_api.cmdb.wireless_controller.ble_profile import BleProfileWcC
from fortigate_api.cmdb.wireless_controller.bonjour_profile import BonjourProfileWcC
from fortigate_api.cmdb.wireless_controller.global_ import GlobalWcC
from fortigate_api.cmdb.wireless_controller.inter_controller import InterControllerWcC
from fortigate_api.cmdb.wireless_controller.log import LogWcC
from fortigate_api.cmdb.wireless_controller.mpsk_profile import MpskProfileWcC
from fortigate_api.cmdb.wireless_controller.qos_profile import QosProfileWcC
from fortigate_api.cmdb.wireless_controller.region import RegionWcC
from fortigate_api.cmdb.wireless_controller.setting import SettingWcC
from fortigate_api.cmdb.wireless_controller.snmp import SnmpWcC
from fortigate_api.cmdb.wireless_controller.timers import TimersWcC
from fortigate_api.cmdb.wireless_controller.utm_profile import UtmProfileWcC
from fortigate_api.cmdb.wireless_controller.vap import VapWcC
from fortigate_api.cmdb.wireless_controller.vap_group import VapGroupWcC
from fortigate_api.cmdb.wireless_controller.wag_profile import WagProfileWcC
from fortigate_api.cmdb.wireless_controller.wids_profile import WidsProfileWcC
from fortigate_api.cmdb.wireless_controller.wtp import WtpWcC
from fortigate_api.cmdb.wireless_controller.wtp_group import WtpGroupWcC
from fortigate_api.cmdb.wireless_controller.wtp_profile import WtpProfileWcC
from fortigate_api.fortigate import FortiGate


class WirelessControllerC:
    """Cmdb/wireless-controller connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init WirelessControllerC."""

        self.access_control_list = AccessControlListWcC(fortigate, **kwargs)
        """:py:class:`.AccessControlListWcC` cmdb/wireless-controller/access-control-list."""

        self.address = AddressWcC(fortigate, **kwargs)
        """:py:class:`.AddressWcC` cmdb/wireless-controller/address."""

        self.addrgrp = AddrgrpWcC(fortigate, **kwargs)
        """:py:class:`.AddrgrpWcC` cmdb/wireless-controller/addrgrp."""

        self.ap_status = ApStatusWcC(fortigate, **kwargs)
        """:py:class:`.ApStatusWcC` cmdb/wireless-controller/ap-status."""

        self.apcfg_profile = ApcfgProfileWcC(fortigate, **kwargs)
        """:py:class:`.ApcfgProfileWcC` cmdb/wireless-controller/apcfg-profile."""

        self.arrp_profile = ArrpProfileWcC(fortigate, **kwargs)
        """:py:class:`.ArrpProfileWcC` cmdb/wireless-controller/arrp-profile."""

        self.ble_profile = BleProfileWcC(fortigate, **kwargs)
        """:py:class:`.BleProfileWcC` cmdb/wireless-controller/ble-profile."""

        self.bonjour_profile = BonjourProfileWcC(fortigate, **kwargs)
        """:py:class:`.BonjourProfileWcC` cmdb/wireless-controller/bonjour-profile."""

        self.global_ = GlobalWcC(fortigate, **kwargs)
        """:py:class:`.GlobalWcC` cmdb/wireless-controller/global."""

        self.inter_controller = InterControllerWcC(fortigate, **kwargs)
        """:py:class:`.InterControllerWcC` cmdb/wireless-controller/inter-controller."""

        self.log = LogWcC(fortigate, **kwargs)
        """:py:class:`.LogWcC` cmdb/wireless-controller/log."""

        self.mpsk_profile = MpskProfileWcC(fortigate, **kwargs)
        """:py:class:`.MpskProfileWcC` cmdb/wireless-controller/mpsk-profile."""

        self.qos_profile = QosProfileWcC(fortigate, **kwargs)
        """:py:class:`.QosProfileWcC` cmdb/wireless-controller/qos-profile."""

        self.region = RegionWcC(fortigate, **kwargs)
        """:py:class:`.RegionWcC` cmdb/wireless-controller/region."""

        self.setting = SettingWcC(fortigate, **kwargs)
        """:py:class:`.SettingWcC` cmdb/wireless-controller/setting."""

        self.snmp = SnmpWcC(fortigate, **kwargs)
        """:py:class:`.SnmpWcC` cmdb/wireless-controller/snmp."""

        self.timers = TimersWcC(fortigate, **kwargs)
        """:py:class:`.TimersWcC` cmdb/wireless-controller/timers."""

        self.utm_profile = UtmProfileWcC(fortigate, **kwargs)
        """:py:class:`.UtmProfileWcC` cmdb/wireless-controller/utm-profile."""

        self.vap = VapWcC(fortigate, **kwargs)
        """:py:class:`.VapWcC` cmdb/wireless-controller/vap."""

        self.vap_group = VapGroupWcC(fortigate, **kwargs)
        """:py:class:`.VapGroupWcC` cmdb/wireless-controller/vap-group."""

        self.wag_profile = WagProfileWcC(fortigate, **kwargs)
        """:py:class:`.WagProfileWcC` cmdb/wireless-controller/wag-profile."""

        self.wids_profile = WidsProfileWcC(fortigate, **kwargs)
        """:py:class:`.WidsProfileWcC` cmdb/wireless-controller/wids-profile."""

        self.wtp = WtpWcC(fortigate, **kwargs)
        """:py:class:`.WtpWcC` cmdb/wireless-controller/wtp."""

        self.wtp_group = WtpGroupWcC(fortigate, **kwargs)
        """:py:class:`.WtpGroupWcC` cmdb/wireless-controller/wtp-group."""

        self.wtp_profile = WtpProfileWcC(fortigate, **kwargs)
        """:py:class:`.WtpProfileWcC` cmdb/wireless-controller/wtp-profile."""
