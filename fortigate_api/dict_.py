"""Tools for Dictionary"""

from urllib.parse import quote

from fortigate_api.types_ import DAny, IStr, LStr, IStrs


def check_mandatory(keys: IStr, **kwargs) -> None:
    """Check all of `keys` are mandatory in `kwargs`
    :param keys: Interested keys, all of them should be in `kwargs`
    :param kwargs: Checked data
    :raises KeyError: If one of the `keys` is not found in `kwargs`
    """
    keys2 = list(kwargs)
    keys_absent: LStr = []
    for key in keys:
        if key not in keys2:
            keys_absent.append(key)
    if keys_absent:
        raise KeyError(f"mandatory {keys_absent=} in {keys2}")


def check_only_one(keys: IStr, **kwargs) -> None:
    """Check only one of keys should be in `kwargs`
    :param keys: Interested keys, only one of them should be in `kwargs`
    :param kwargs: Checked data
    :raises KeyError: If multiple of the `keys` are found in `kwargs`
    """
    keys1 = set(keys)
    keys2 = set(kwargs)
    intersection = keys1.intersection(keys2)
    if len(intersection) > 1:
        raise KeyError(f"multiple keys={intersection} not allowed in {keys2}, expected only one")


def check_one_of(keys: IStr, **kwargs) -> None:
    """Check one of key is mandatory in `kwargs`
    :param keys: Interested keys, one of them should be in `kwargs`
    :param kwargs: Checked data
    :raises KeyError: If none of the `keys` are found in `kwargs`
    """
    if not keys:
        return
    keys2 = set(kwargs)
    for key in keys:
        if key in keys2:
            return
    raise KeyError(f"mandatory one of {keys=} in {keys2}")


def get_quoted(key: str, **kwargs) -> str:
    """Get mandatory key/value from `kwargs` and returns quoted value as *str_*
    :param key: Interested `key` in `kwargs`
    :param kwargs: Data
    :return: Interested quoted value
    """
    check_mandatory(keys=[key], **kwargs)
    value = str(kwargs[key])
    quoted = quote(string=value, safe="")
    return quoted


def pop_int(key: str, data: DAny) -> int:
    """Pops key/value from `data` and returns value as *int*
    :param key: Interested `key` in `data`
    :param data: Data
    :return: Interested value. Side effect `data` - removes interested 'key'
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
    """Pops key/value from `data` and returns value as *List[str_]*
    :param key: Interested `key` in `data`
    :param data: Data
    :return: Interested value. Side effect `data` - removes interested 'key'
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
    """Pops key/value from `data` and returns value as *str_*
    :param key: Interested `key` in `data`
    :param data: Data
    :return: Interested value. Side effect `data` - removes interested 'key'
    """
    if key not in data:
        return ""
    value = data.pop(key)
    if value is None:
        value = ""
    return str(value)


def pop_quoted(key: str, data: DAny) -> str:
    """Pops key/value from `data` and returns quoted value as *str_*
    :param key: Interested `key` in `data`
    :param data: Data
    :return: Interested value. Side effect `data` - removes interested 'key'
    """
    if key not in data:
        return ""
    value = data.pop(key)
    if value is None:
        return ""
    return quote(string=str(value), safe="")
