"""Types."""

from datetime import date
from ipaddress import IPv4Network
from pathlib import Path
from typing import Any, Dict, Iterable, List, Literal, Optional, Set, Tuple, Union
from requests import Response

# values
Method = Literal["delete", "get", "post", "put"]

# 1 level
DAny = Dict[str, Any]
DStr = Dict[str, str]
IStr = Iterable[str]
LPath = List[Path]
LResponse = List[Response]
LStr = List[str]
SDate = Set[date]
SStr = Set[str]
StrInt = Union[str, int]
T2Str = Tuple[str, str]
T3Str = Tuple[str, str, str]
TLists = (list, set, tuple)

# 2 level
DDAny = Dict[str, DAny]
DLStr = Dict[str, LStr]
LDAny = List[DAny]
LTup2 = List[T2Str]
ODAny = Optional[DAny]
UStr = Union[str, IStr]

# ipaddress
DLInet = Dict[str, List[IPv4Network]]
DSInet = Dict[IPv4Network, SStr]
