"""Test fortigate_api.py"""
import re
from typing import Callable

import pytest
from requests import Session

from fortigate_api import FortiGateAPI
from fortigate_api import helpers as h

QUERY = "api/v2/cmdb/firewall/policy"
TAB = "    "
IP = "172.16.177.65"


@pytest.fixture
def api():
    """Init FortiGateAPI"""
    api_o = FortiGateAPI(host="host")
    api_o.fortigate._session = Session()
    return api_o


# ============================= helpers ==============================


def test__get_scopes(api: FortiGateAPI):
    """FortiGateAPI._get_scopes()"""
    actual = api._get_scopes()
    assert actual == ["cmdb", "log", "monitor"]


def test__scope_docstring(api: FortiGateAPI):
    """FortiGateAPI scope class docstring.

    :example:
        scope: "cmdb"
        actual: "Cmdb scope."
    """
    for scope in api._get_scopes():
        scope_o = getattr(api, scope)
        actual = scope_o.__doc__
        actual = actual.splitlines()[0]

        expected = f"{scope} scope connectors.".capitalize()
        assert actual == expected


def test__scope_init_docstring(api: FortiGateAPI):
    """FortiGateAPI scope.__init__ docstring.

    :example:
        scope: "cmdb", app: "firewall"
        actual: "Init CmdbS."
    """
    for scope in api._get_scopes():
        scope_o = getattr(api, scope)
        actual = scope_o.__init__.__doc__

        expected = str(scope).lower().capitalize() + "S"
        expected = f"Init {expected}."
        assert actual == expected


def test__app_docstring(api: FortiGateAPI):
    """FortiGateAPI scope.app class docstring.
    
    :example:
        scope: "cmdb", app: "firewall"
        actual: "``cmdb/firewall/`` connectors."
    """
    for scope in api._get_scopes():
        scope_o = getattr(api, scope)
        apps = [s for s in dir(scope_o) if s[0].islower()]
        for app in apps:
            app_o = getattr(scope_o, app)
            actual = app_o.__doc__
            actual = actual.replace("_", ".").replace("-", ".")

            # expected
            expected = f"{scope}/{app} connectors.".capitalize()
            expected = expected.replace("_", ".").replace("-", ".")
            assert actual == expected


def test__scope_app_init_docstring(api: FortiGateAPI):
    """FortiGateAPI scope.app.__init__ docstring.

    :example:
        scope: "cmdb", app: "firewall"
        actual: "Init FirewallC."
    """
    for scope in api._get_scopes():
        scope_o = getattr(api, scope)
        apps = [s for s in dir(scope_o) if s[0].islower()]
        for app in apps:
            actual = getattr(scope_o, app).__init__.__doc__

            # expected
            class_name = "".join([s.lower().capitalize() for s in app.split("_")])
            class_name = class_name + scope[0].upper()
            expected = f"Init {class_name}."
            assert actual == expected


def test__model(api: FortiGateAPI):
    """FortiGateAPI scope.app.model.

    :example:
        scope: "cmdb", app: "firewall", model="address",
        actual: "``cmdb/firewall/address`` connector."
    """
    for scope in api._get_scopes():
        scope_o = getattr(api, scope)
        apps = [s for s in dir(scope_o) if s[0].islower()]
        for app in apps:
            app_o = getattr(scope_o, app)
            models = [s for s in dir(app_o) if s[0].islower()]

            for model in models:
                _test__model_docstring(scope, app, app_o, model)
                _test__model_name(app_o, model)


def _test__model_docstring(scope: str, app: str, app_o: Callable, model: str):
    """FortiGateAPI scope.app.model docstring"""
    model_o = getattr(app_o, model)
    if model in ["global_"]:
        model = model[:-1]
    actual_doc = model_o.__doc__
    actual_doc = actual_doc.replace("+", "")  # tacacs+
    re_docstring = f"^{scope.capitalize()}/{app}/{model} connector.$"
    re_docstring = re_docstring.replace("-", ".").replace("_", ".")

    actual = bool(re.search(re_docstring, actual_doc))
    assert actual


# noinspection PyProtectedMember
def _test__model_name(app_o: Callable, model: str):
    """FortiGateAPI scope.app.model name"""
    model_o = getattr(app_o, model)
    scope_name, app_name, model_name = h.path_to_parts(model_o._path)
    _, expected = h.model_names(scope_name, app_name, model_name)
    actual = model_o.__class__.__name__

    assert model == model.lower()
    assert actual == expected
