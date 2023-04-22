"""Types."""

from datetime import date
from ipaddress import IPv4Network
from pathlib import Path
from typing import Any, Dict, Iterable, List, Literal, Set, Tuple, Union

from requests import Response

DAny = Dict[str, Any]
DStr = Dict[str, str]
IStr = Iterable[str]
LPath = List[Path]
LResponse = List[Response]
LStr = List[str]
Method = Literal["delete", "get", "post", "put"]
SDate = Set[date]
SStr = Set[str]
StrInt = Union[str, int]
T2Str = Tuple[str, str]
T3Str = Tuple[str, str, str]

DDAny = Dict[str, DAny]
DLInet = Dict[str, List[IPv4Network]]
DLStr = Dict[str, LStr]
DSInet = Dict[IPv4Network, SStr]
IStrs = Union[str, IStr]
LDAny = List[DAny]
LTup2 = List[T2Str]
UStr = Union[str, IStr]
