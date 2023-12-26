"""Test extended_filters.py"""
import pytest
from pytest_mock import MockerFixture
from requests import Session

from fortigate_api import extended_filters, FortigateAPI
from tests import helpers__efilters as efilters


@pytest.fixture
def connectors():
    """Init Connector objects."""
    api = FortigateAPI(host="host")
    api.rest._session = Session()
    items = [
        api.policy,
    ]
    return items


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
def test__valid_efilters(efilters, error):
    """extended_filters._valid_efilters()"""
    if error is None:
        extended_filters._valid_efilters(efilters=efilters)
    else:
        with pytest.raises(error):
            extended_filters._valid_efilters(efilters=efilters)


@pytest.mark.parametrize("kwargs, expected", [
    (dict(efilter="srcaddr==10.0.0.0/30"), ["POL1"]),
    (dict(efilter="srcaddr==10.0.0.0/29"), []),
    (dict(efilter="srcaddr!=10.0.0.0/30"), ["POL3"]),
    (dict(efilter="srcaddr!=10.0.0.0/29"), ["POL1", "POL3"]),
    (dict(efilter="srcaddr<=10.0.0.0/32"), []),  # get all subnets
    (dict(efilter="srcaddr<=10.0.0.0/31"), []),
    (dict(efilter="srcaddr<=10.0.0.0/30"), ["POL1"]),
    (dict(efilter="srcaddr<=10.0.0.0/29"), ["POL1", "POL3"]),
    (dict(efilter="srcaddr<=0.0.0.0/0"), ["POL1", "POL3"]),
    (dict(efilter="srcaddr>=10.0.0.0"), ["POL1"]),  # get all supernets
    (dict(efilter="srcaddr>=10.0.0.0/32"), ["POL1"]),
    (dict(efilter="srcaddr>=10.0.0.0/31"), ["POL1"]),
    (dict(efilter="srcaddr>=10.0.0.0/30"), ["POL1"]),
    (dict(efilter="srcaddr>=10.0.0.0/29"), []),
    (dict(efilter="srcaddr>=0.0.0.0/0"), []),
    (dict(name="POL1"), KeyError),
    (dict(efilter="srcaddr=!10.0.0.0/30"), ValueError),
    (dict(efilter="typo==10.0.0.0/30"), ValueError),
    (dict(efilter="srcaddr==typo"), ValueError),
    (dict(efilter="srcaddr==10.0.0.1000"), ValueError),
    (dict(efilter="srcaddr==10.0.0.1/33"), ValueError),
    (dict(efilter="srcaddr==fd12:3456:789a:1::/64"), ValueError),
])
def test__get(connectors: list, mocker: MockerFixture, kwargs, expected):
    """Policy.get()"""
    mocker.patch("requests.Session.get",
                 side_effect=lambda *args, **kw: efilters.session_get(mocker, *args, **kw))

    for connector in connectors:
        if isinstance(expected, list):
            items = connector.get(**kwargs)
            actual = [d["name"] for d in items]
            assert actual == expected
        else:
            with pytest.raises(expected):
                connector.get(**kwargs)
