"""Cmdb/wireless-controller.hotspot20 connectors."""

from fortigate_api.cmdb.wireless_controller_hotspot20.anqp_3gpp_cellular import Anqp3gppCellularWchC
from fortigate_api.cmdb.wireless_controller_hotspot20.anqp_ip_address_type import (
    AnqpIpAddressTypeWchC,
)
from fortigate_api.cmdb.wireless_controller_hotspot20.anqp_nai_realm import AnqpNaiRealmWchC
from fortigate_api.cmdb.wireless_controller_hotspot20.anqp_network_auth_type import (
    AnqpNetworkAuthTypeWchC,
)
from fortigate_api.cmdb.wireless_controller_hotspot20.anqp_roaming_consortium import (
    AnqpRoamingConsortiumWchC,
)
from fortigate_api.cmdb.wireless_controller_hotspot20.anqp_venue_name import AnqpVenueNameWchC
from fortigate_api.cmdb.wireless_controller_hotspot20.h2qp_conn_capability import (
    H2qpConnCapabilityWchC,
)
from fortigate_api.cmdb.wireless_controller_hotspot20.h2qp_operator_name import H2qpOperatorNameWchC
from fortigate_api.cmdb.wireless_controller_hotspot20.h2qp_osu_provider import H2qpOsuProviderWchC
from fortigate_api.cmdb.wireless_controller_hotspot20.h2qp_wan_metric import H2qpWanMetricWchC
from fortigate_api.cmdb.wireless_controller_hotspot20.hs_profile import HsProfileWchC
from fortigate_api.cmdb.wireless_controller_hotspot20.icon import IconWchC
from fortigate_api.cmdb.wireless_controller_hotspot20.qos_map import QosMapWchC
from fortigate_api.fortigate import FortiGate


class WirelessControllerHotspot20C:
    """Cmdb/wireless-controller.hotspot20 connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init WirelessControllerHotspot20C."""

        self.anqp_3gpp_cellular = Anqp3gppCellularWchC(fortigate, **kwargs)
        """:py:class:`.Anqp3gppCellularWchC` 
            cmdb/wireless-controller.hotspot20/anqp-3gpp-cellular.
        """

        self.anqp_ip_address_type = AnqpIpAddressTypeWchC(fortigate, **kwargs)
        """:py:class:`.AnqpIpAddressTypeWchC` 
            cmdb/wireless-controller.hotspot20/anqp-ip-address-type.
        """

        self.anqp_nai_realm = AnqpNaiRealmWchC(fortigate, **kwargs)
        """:py:class:`.AnqpNaiRealmWchC` cmdb/wireless-controller.hotspot20/anqp-nai-realm."""

        self.anqp_network_auth_type = AnqpNetworkAuthTypeWchC(fortigate, **kwargs)
        """:py:class:`.AnqpNetworkAuthTypeWchC` 
            cmdb/wireless-controller.hotspot20/anqp-network-auth-type.
        """

        self.anqp_roaming_consortium = AnqpRoamingConsortiumWchC(fortigate, **kwargs)
        """:py:class:`.AnqpRoamingConsortiumWchC` 
            cmdb/wireless-controller.hotspot20/anqp-roaming-consortium.
        """

        self.anqp_venue_name = AnqpVenueNameWchC(fortigate, **kwargs)
        """:py:class:`.AnqpVenueNameWchC` cmdb/wireless-controller.hotspot20/anqp-venue-name."""

        self.h2qp_conn_capability = H2qpConnCapabilityWchC(fortigate, **kwargs)
        """:py:class:`.H2qpConnCapabilityWchC` 
            cmdb/wireless-controller.hotspot20/h2qp-conn-capability.
        """

        self.h2qp_operator_name = H2qpOperatorNameWchC(fortigate, **kwargs)
        """:py:class:`.H2qpOperatorNameWchC` 
            cmdb/wireless-controller.hotspot20/h2qp-operator-name.
        """

        self.h2qp_osu_provider = H2qpOsuProviderWchC(fortigate, **kwargs)
        """:py:class:`.H2qpOsuProviderWchC` cmdb/wireless-controller.hotspot20/h2qp-osu-provider."""

        self.h2qp_wan_metric = H2qpWanMetricWchC(fortigate, **kwargs)
        """:py:class:`.H2qpWanMetricWchC` cmdb/wireless-controller.hotspot20/h2qp-wan-metric."""

        self.hs_profile = HsProfileWchC(fortigate, **kwargs)
        """:py:class:`.HsProfileWchC` cmdb/wireless-controller.hotspot20/hs-profile."""

        self.icon = IconWchC(fortigate, **kwargs)
        """:py:class:`.IconWchC` cmdb/wireless-controller.hotspot20/icon."""

        self.qos_map = QosMapWchC(fortigate, **kwargs)
        """:py:class:`.QosMapWchC` cmdb/wireless-controller.hotspot20/qos-map."""
