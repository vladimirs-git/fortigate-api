"""Typing"""
from typing import Any, Dict, Iterable, List, Tuple, Union

DAny = Dict[str, Any]
DStr = Dict[str, str]
IStr = Iterable[str]
LStr = List[str]
StrInt = Union[str, int]
Tup2 = Tuple[str, str]

IStrs = Union[str, IStr]
LDAny = List[DAny]
LTup2 = List[Tup2]
