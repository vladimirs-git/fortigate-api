"""Helper functions."""

import time
from operator import attrgetter
from urllib import parse
from urllib.parse import urlencode, urlparse, parse_qs, ParseResult

from requests import Response
from vhelpers import vdict, vlist

from fortigate_api.types_ import Any, DAny, SeqStr, LStr, LResponse
from fortigate_api.types_ import StrInt, UStr, TLists, T3Str, T2Str


# ========================= scope app model ==========================


def scope_names(scope: str) -> T3Str:
    """Create class name for scope.

    :example:
        scope_names("cmdb") -> "cmdb", "cmdb_s", "CmdbS"
    """
    scope_name = part_to_attr(scope)
    scope_class = scope.capitalize() + "S"
    scope_file = scope + "_s"
    return scope_name, scope_file, scope_class


def app_names(scope: str, app: str) -> T3Str:
    """Create class name for app.

    :example:
        app_names("cmdb", "firewall") -> "firewall", "firewall_c", "FirewallC"
    """
    scope_name = part_to_attr(scope)
    app_name = part_to_attr(app)

    scope_char = scope_name[0].upper()
    app_class = "".join([s.capitalize() for s in app_name.split("_")])
    app_class += scope_char
    app_file = app_name + "_" + scope_char.lower()
    return app_name, app_file, app_class


def model_names(scope: str, app: str, model: str) -> T2Str:
    """Create class name for model.

    :example:
        model_names("cmdb", "firewall", "address") -> address, "AddressFC"
    """
    scope_name = part_to_attr(scope)
    app_name = part_to_attr(app)
    model_name = part_to_attr(model)

    reserved_keywords = ["global"]
    if model_name in reserved_keywords:
        model_name += "_"
    scope_char = scope_name[0].upper()
    app_char = "".join([s[0] for s in app_name.split("_")])
    app_char = app_char.capitalize()
    model_class = "".join([s.capitalize() for s in model_name.split("_")])
    if model_class[0].isdigit():
        model_class = f"_{model_class}"
    model_class = model_class + app_char + scope_char
    return model_name, model_class


def part_to_attr(part: str) -> str:
    """Convert path part to attribute name.

    :param part: The path part to be converted.

    :return: The converted attribute name.

    :example:
        part_to_attr("firewall.ssh") -> "firewall_ssh"
    """
    attr = part.lower()
    items = vlist.split(attr, ignore="_")
    attr = "_".join(items)
    if attr[0].isdigit():
        attr = f"_{attr}"
    return attr


def attr_to_app(attr: str) -> str:
    """Convert attribute name to app name.

    :param attr: The attribute name to be converted.

    :return: The converted app name.

    :example:
        attr_to_app("firewall_ssh") -> "firewall.ssh"
    """
    return attr.replace("_", ".")


def attr_to_model(attr: str) -> str:
    """Convert attribute name to model name.

    :param attr: The attribute name to be converted.

    :return: The converted model name.

    :example:
        attr_to_model("local_ca") -> "local-ca"
    """
    return attr.replace("_", "-")


def path_to_attrs(path: str) -> T3Str:
    """Convert path scope/app/model to attribute names.

    :param path: The path to be converted.

    :return: Tuple of converted attribute names.

    :example:
        path_to_attrs("/cmdb/firewall.ssh/local-ca") -> "cmdb", "firewall_ssh", "local_ca"
    """
    scope, app, model = path_to_parts(path)
    app = part_to_attr(app)
    model = part_to_attr(model)
    return scope, app, model


def path_to_parts(path: str) -> T3Str:
    """Convert path scope/app/model to path parts.

    :param path: The path to be converted.

    :return: Tuple of converted part names.

    :example:
        path_to_parts("/cmdb/firewall.ssh/local-ca") -> "cmdb", "firewall.ssh", local-ca
    """
    path = path.strip("/")
    if path.startswith("api/v2/"):
        path = path.replace("api/v2/", "", 1)
    items = path.split("/")
    if len(items) == 3:
        scope = items[0]
        app = items[1]
        model = items[2]
    elif len(items) == 2:
        scope = ""
        app = items[0]
        model = items[1]
    else:
        raise ValueError(f"Invalid {path=}.")
    return scope, app, model


# =============================== dict ===============================


def check_mandatory(keys: SeqStr, **kwargs) -> None:
    """Check all of `keys` are mandatory in `kwargs`.

    :param keys: Interested keys, all of them should be in `kwargs`.
    :param kwargs: Checked data.
    :raises KeyError: If one of the `keys` is not found in `kwargs`.
    """
    keys_absent: LStr = []
    for key in keys:
        if key not in kwargs:
            keys_absent.append(key)
    if keys_absent:
        raise KeyError(f"Mandatory {keys_absent=} in {list(kwargs)}.")


def check_only_one(keys: SeqStr, **kwargs) -> None:
    """Check only one of keys should be in `kwargs`.

    :param keys: Interested keys, only one of them should be in `kwargs`.
    :param kwargs: Checked data.
    :raises KeyError: If multiple of the `keys` are found in `kwargs`.
    """
    keys1 = set(keys)
    allowed = set(kwargs)
    intersection = keys1.intersection(allowed)
    if len(intersection) > 1:
        raise KeyError(f"Expected only one key, {intersection} are not allowed in {allowed}.")


def check_one_of(keys: SeqStr, **kwargs) -> None:
    """Check one of key is mandatory in `kwargs`.

    :param keys: Interested keys, one of them should be in `kwargs`.
    :param kwargs: Checked data.
    :raises KeyError: If none of the `keys` are found in `kwargs`.
    """
    if not keys:
        return
    for key in keys:
        if key in kwargs:
            return
    raise KeyError(f"Mandatory one of {keys=} in {list(kwargs)}.")


# noinspection PyShadowingBuiltins
def check_uid_filter(
    uid: StrInt = "",
    filter: UStr = "",  # pylint: disable=redefined-builtin
) -> None:
    """Check `uid` and `filter` parameters."""
    params = ["uid", "filter"]
    if not (uid or filter):
        raise ValueError(f"One of {params} is required.")
    if uid and filter:
        raise ValueError(f"Only one of {params} is expected.")


def pop_lstr(key: str, data: DAny) -> LStr:
    """Pop list of strings key/value from `data`.

    If key is absent in data return empty list.

    :param key: The `key` to be popped from `data`.
    :param data: The dictionary from which the key is to be popped.
    :return: The values as a string. Update `data`, remove `key`.
    """
    values = vdict.pop(data, key=key)
    if values is None:
        values = []
    if isinstance(values, str):
        values = [values]
    if not isinstance(values, TLists):
        raise TypeError(f"{key=} {values=} {list} expected.")
    for value in values:
        if not isinstance(value, str):
            raise TypeError(f"{key=} {value=} {list} expected.")
    return list(values)


# =============================== str ================================


def join_url_params(url: str, **params) -> str:
    """Add params to URL.

    :param url: URL with old params.
    :param params: New params.
    :return: URL with old and new params.

    :example:
        url: "https://fomain.com?a=a"
        params: {"b": ["b", "B"]}
        return: "https://fomain.com?a=a&b=b&b=B"
    """
    url_o: ParseResult = urlparse(url)
    params_old: DAny = parse_qs(url_o.query)
    params_new: DAny = {**params_old, **params}
    query: str = urlencode(params_new, doseq=True)
    url_o = url_o._replace(query=query)
    return url_o.geturl()


def quote(string: Any) -> str:
    """Quote name of the string.

    :param string: Line to by quoted
    :example: "10.0.0.0/8" > "10.0.0.0%2F8"
    """
    if string is None:
        return ""
    string = str(string)
    return parse.quote(string=string, safe="")


def url_join(base: str, path: StrInt) -> str:
    """Join path segments to a base URL safely using slash."""
    path_ = str(path)
    if not path_:
        return base
    return base.rstrip("/") + "/" + path_.lstrip("/")


def url_to_app_model(url: str) -> str:
    """Parse app/model name from the URL.

    :param url: The URL to parse.
    :return: The app/model name parsed from the URL.
    :example:
        url_to_model("https://domain.com/api/v2/cmdb/firewall/policy/1") -> "firewall/policy"
    """
    url_o: ParseResult = urlparse(url)
    path = url_o.path.strip("/")
    items = path.split("/")
    if len(items) <= 4:
        return ""
    app = items[3]
    model = items[4]
    return f"{app}/{model}"


def url_to_uid(url: str) -> str:
    """Parse UID name from the URL.

    :param url: The URL to parse.
    :return: The UID parsed from the URL.
    :example:
        url_to_uuid("https://domain.com/api/v2/cmdb/firewall/policy/1") -> "1"
    """
    url_o: ParseResult = urlparse(url)
    path = url_o.path.strip("/")
    items = path.split("/")
    if len(items) <= 5:
        return ""
    model = items[5]
    return model


def rst_code(text: str, code: str = "python") -> str:
    """Wrap text to restructuredtext code pyton."""
    tab = "    "
    lines = [
        f".. code:: {code}",
        "",
        *[f"{tab}{s}" for s in text.splitlines()],
        "",
    ]
    return "\n".join(lines)


# ============================= unsorted ==============================


def highest_response(responses: LResponse) -> Response:
    """Return Response object with the highest status_code.

    :param responses: List of Response objects.
    :type responses: List[Response]

    :return: Response with the highest (worst) status_code or <Response [404]>.
        If no objects have been found, return <Response [404]>.
    :rtype: Response
    """
    if responses:
        responses = sorted(responses, key=attrgetter("status_code"))
        return responses[-1]
    response = Response()
    response.status_code = 404
    return response


# ============================= wrapper ==============================


def time_spent(func):
    """Wrap measure function execution time."""

    def wrap(*args, **kwargs):
        """Wrap."""
        started = time.time()
        pattern = "====== {:s}, spent {:.3f}s ======"
        try:
            _return = func(*args, **kwargs)
        except Exception:
            elapsed = time.time() - started
            print(pattern.format(func.__name__, elapsed))
            raise
        elapsed = time.time() - started
        print(pattern.format(func.__name__, elapsed))
        return _return

    return wrap
