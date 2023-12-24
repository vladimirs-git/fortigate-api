"""Helper functions."""

import os
import re
import time
from datetime import datetime
from urllib import parse
from urllib.parse import urlencode, urlparse, parse_qs, ParseResult

from fortigate_api.types_ import Any, DAny, T2Str, T3Str, IStr, IStrs, LStr, SDate


# =============================== dict ===============================

def check_mandatory(keys: IStr, **kwargs) -> None:
    """Check all of `keys` are mandatory in `kwargs`.

    :param keys: Interested keys, all of them should be in `kwargs`.
    :param kwargs: Checked data.
    :raises KeyError: If one of the `keys` is not found in `kwargs`.
    """
    keys2 = list(kwargs)
    keys_absent: LStr = []
    for key in keys:
        if key not in keys2:
            keys_absent.append(key)
    if keys_absent:
        raise KeyError(f"mandatory {keys_absent=} in {keys2}")


def check_only_one(keys: IStr, **kwargs) -> None:
    """Check only one of keys should be in `kwargs`.

    :param keys: Interested keys, only one of them should be in `kwargs`.
    :param kwargs: Checked data.
    :raises KeyError: If multiple of the `keys` are found in `kwargs`.
    """
    keys1 = set(keys)
    keys2 = set(kwargs)
    intersection = keys1.intersection(keys2)
    if len(intersection) > 1:
        raise KeyError(f"multiple keys={intersection} not allowed in {keys2}, expected only one")


def check_one_of(keys: IStr, **kwargs) -> None:
    """Check one of key is mandatory in `kwargs`.

    :param keys: Interested keys, one of them should be in `kwargs`.
    :param kwargs: Checked data.
    :raises KeyError: If none of the `keys` are found in `kwargs`.
    """
    if not keys:
        return
    keys2 = set(kwargs)
    for key in keys:
        if key in keys2:
            return
    raise KeyError(f"mandatory one of {keys=} in {keys2}")


def get_quoted(key: str, **kwargs) -> str:
    """Get mandatory key/value from `kwargs` and return quoted value as string.

    :param key: Interested `key` in `kwargs`.
    :param kwargs: Data.
    :return: Interested quoted value.
    """
    check_mandatory(keys=[key], **kwargs)
    value = str(kwargs[key])
    quoted = parse.quote(string=value, safe="")
    return quoted


def pop_int(key: str, data: DAny) -> int:
    """Pop key/value from `data` and return value as integer.

    :param key: Interested `key` in `data`.
    :param data: Data.
    :return: Interested value. Side effect `data` - removes interested 'key'.
    """
    if key not in data:
        return 0
    value = data.pop(key)
    if not value:
        value = "0"
    value = str(value)
    if not value.isdigit():
        raise TypeError(f"{key}={value} {int} expected")
    return int(value)


def pop_lstr(key: str, data: DAny) -> LStr:
    """Pop key/value from `data` and return value as List[str].

    :param key: Interested `key` in `data`.
    :param data: Data.
    :return: Interested value. Side effect `data` - removes interested 'key'.
    """
    if key not in data:
        return []
    values: IStrs = data.pop(key)
    if not isinstance(values, (str, list, set, tuple)):
        raise TypeError(f"{key}={values} {list} expected")
    if isinstance(values, str):
        values = [values]
    if invalid := [s for s in values if not isinstance(s, str)]:
        raise TypeError(f"{key}={invalid} {str} expected")
    return list(values)


def pop_str(key: str, data: DAny) -> str:
    """Pop key/value from `data` and return value as string.

    :param key: Interested `key` in `data`.
    :param data: Data.
    :return: Interested value. Side effect `data` - removes interested 'key'.
    """
    if key not in data:
        return ""
    value = data.pop(key)
    if value is None:
        value = ""
    return str(value)


def pop_quoted(key: str, data: DAny) -> str:
    """Pop key/value from `data` and return quoted value as string.

    :param key: Interested `key` in `data`.
    :param data: Data.
    :return: Interested value. Side effect `data` - removes interested 'key'.
    """
    if key not in data:
        return ""
    value = data.pop(key)
    if value is None:
        return ""
    return parse.quote(string=str(value), safe="")


# =============================== str ================================

def attr_to_class(attr: str) -> str:
    """Replace lower-case attribute name camel-case class name.

    :param attr: Attribute name.

    :return: class name.

    :example: attr_to_class("address_group") -> "AddressGroup"
    """
    return "".join([s.capitalize() for s in attr.split("_")])


def class_to_attr(word: str) -> str:
    """Replace upper character with underscore and lower.

    :param word: The word to be modified.

    :return: The modified word.

    :example: replace_upper("IpAddresses") -> "ip_addresses"
    """
    if not word:
        return ""
    word = word[0].lower() + word[1:]
    new_word = ""
    for char in word:
        if char.isupper():
            new_word += "_" + char.lower()
        else:
            new_word += char
    return new_word


def make_url(url: str, **params) -> str:
    """Add params to URL.

    :param url: URL with old params
    :param params: New params
    :return: URL with old and new params

    :example:
        url: "https://fomain.com?a=a"
        params: {"b": ["b", "B"]}
        return: "https://fomain.com?a=a&b=b&b=B"
    """
    url_o: ParseResult = urlparse(url)
    params_or: DAny = parse_qs(url_o.query)
    params_: DAny = {**params_or, **params}
    query: str = urlencode(params_, doseq=True)
    url_o = url_o._replace(query=query)
    return url_o.geturl()


def quote(string: Any) -> str:
    """Quote name of the string.

    :param string: Line to by quoted
    :example: "10.0.0.0/8" > "10.0.0.0%2F8"
    """
    return parse.quote(string=str(string), safe="")


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


# ============================= unsorted =============================

def files_py(root: str) -> LStr:
    """Paths to .py file."""
    paths: LStr = []
    for root_i, _, files_i in os.walk(root):
        for file_ in files_i:
            if file_.endswith(".py"):
                path = os.path.join(root_i, file_)
                paths.append(path)
    return paths


def last_modified_date(root: str) -> str:
    """Paths to .py files with last modified dates."""
    dates: SDate = set()
    paths = files_py(root)
    for path in paths:
        stat = os.stat(path)
        date_ = datetime.fromtimestamp(stat.st_mtime).date()
        dates.add(date_)
    if not dates:
        return ""
    date_max = max(dates)
    return str(date_max)
