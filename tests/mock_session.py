"""mocked Session"""

from __future__ import annotations

from requests import Response  # type: ignore

from tests.mock_response import MockResponse


class MockSession:
    """mocked Session"""

    # noinspection PyUnusedLocal
    @staticmethod
    def delete(url: str, **kwargs) -> Response:
        """mocked Session.delete()"""
        return MockResponse.delete(url=url)

    # noinspection PyUnusedLocal
    @staticmethod
    def get(url: str, **kwargs) -> Response:
        """mocked Session.get()"""
        return MockResponse.get(url=url)

    # noinspection PyUnusedLocal
    @staticmethod
    def post(url: str, **kwargs) -> Response:
        """mocked Session.post()"""
        return MockResponse().post(url=url, **kwargs)

    # noinspection PyUnusedLocal
    @staticmethod
    def put(url: str, **kwargs) -> Response:
        """mocked Session.put()"""
        return MockResponse().put(url=url, **kwargs)
