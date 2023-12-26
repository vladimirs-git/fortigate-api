"""Test fortigate_api.py"""

from fortigate_api import FortigateAPI


def test__enter__():
    """FortigateAPI.__enter__() FortigateAPI.__exit__()"""
    api = FortigateAPI(host="host")
    session = api.rest._session
    assert session is None

    with FortigateAPI(host="host") as api:
        session = api.rest._session
        assert session is None
