"""unittest extended_filters.py"""
import pytest

from fortigate_api import extended_filters


@pytest.mark.parametrize("efilters, error", [
    (["srcaddr==1.1.1.1/32"], None),
    (["srcaddr!=1.1.1.1/32"], None),
    (["srcaddr<=1.1.1.1/32"], None),
    (["srcaddr>=1.1.1.1/32"], None),
    (["dstaddr==1.1.1.1/32"], None),
    (["dstaddr!=1.1.1.1/32"], None),
    (["dstaddr<=1.1.1.1/32"], None),
    (["dstaddr>=1.1.1.1/32"], None),
    (["srcaddr==1.1.1.1/32", "dstaddr==2.2.2.2/32"], None),
    (["srcaddr!!1.1.1.1/32"], ValueError),
    (["typo==1.1.1.1/32"], ValueError),
    (["srcaddr==1.1.1.1/32", "srcaddr==2.2.2.2/32"], ValueError),
])
def test__delete(efilters, error):
    """extended_filters._valid_efilters()"""
    if error is None:
        extended_filters._valid_efilters(efilters=efilters)
    else:
        with pytest.raises(error):
            extended_filters._valid_efilters(efilters=efilters)
