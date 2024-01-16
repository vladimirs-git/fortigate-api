"""Cmdb/webfilter connectors."""

from fortigate_api.cmdb.webfilter.content import ContentWC
from fortigate_api.cmdb.webfilter.content_header import ContentHeaderWC
from fortigate_api.cmdb.webfilter.fortiguard import FortiguardWC
from fortigate_api.cmdb.webfilter.ftgd_local_cat import FtgdLocalCatWC
from fortigate_api.cmdb.webfilter.ftgd_local_rating import FtgdLocalRatingWC
from fortigate_api.cmdb.webfilter.ips_urlfilter_cache_setting import IpsUrlfilterCacheSettingWC
from fortigate_api.cmdb.webfilter.ips_urlfilter_setting import IpsUrlfilterSettingWC
from fortigate_api.cmdb.webfilter.ips_urlfilter_setting6 import IpsUrlfilterSetting6WC
from fortigate_api.cmdb.webfilter.override import OverrideWC
from fortigate_api.cmdb.webfilter.profile import ProfileWC
from fortigate_api.cmdb.webfilter.search_engine import SearchEngineWC
from fortigate_api.cmdb.webfilter.urlfilter import UrlfilterWC
from fortigate_api.fortigate import FortiGate


class WebfilterC:
    """Cmdb/webfilter connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init WebfilterC."""

        self.content = ContentWC(fortigate, **kwargs)
        """:py:class:`.ContentWC` cmdb/webfilter/content."""

        self.content_header = ContentHeaderWC(fortigate, **kwargs)
        """:py:class:`.ContentHeaderWC` cmdb/webfilter/content-header."""

        self.fortiguard = FortiguardWC(fortigate, **kwargs)
        """:py:class:`.FortiguardWC` cmdb/webfilter/fortiguard."""

        self.ftgd_local_cat = FtgdLocalCatWC(fortigate, **kwargs)
        """:py:class:`.FtgdLocalCatWC` cmdb/webfilter/ftgd-local-cat."""

        self.ftgd_local_rating = FtgdLocalRatingWC(fortigate, **kwargs)
        """:py:class:`.FtgdLocalRatingWC` cmdb/webfilter/ftgd-local-rating."""

        self.ips_urlfilter_cache_setting = IpsUrlfilterCacheSettingWC(fortigate, **kwargs)
        """:py:class:`.IpsUrlfilterCacheSettingWC` cmdb/webfilter/ips-urlfilter-cache-setting."""

        self.ips_urlfilter_setting = IpsUrlfilterSettingWC(fortigate, **kwargs)
        """:py:class:`.IpsUrlfilterSettingWC` cmdb/webfilter/ips-urlfilter-setting."""

        self.ips_urlfilter_setting6 = IpsUrlfilterSetting6WC(fortigate, **kwargs)
        """:py:class:`.IpsUrlfilterSetting6WC` cmdb/webfilter/ips-urlfilter-setting6."""

        self.override = OverrideWC(fortigate, **kwargs)
        """:py:class:`.OverrideWC` cmdb/webfilter/override."""

        self.profile = ProfileWC(fortigate, **kwargs)
        """:py:class:`.ProfileWC` cmdb/webfilter/profile."""

        self.search_engine = SearchEngineWC(fortigate, **kwargs)
        """:py:class:`.SearchEngineWC` cmdb/webfilter/search-engine."""

        self.urlfilter = UrlfilterWC(fortigate, **kwargs)
        """:py:class:`.UrlfilterWC` cmdb/webfilter/urlfilter."""
