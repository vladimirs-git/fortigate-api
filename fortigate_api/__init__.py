"""fortigate-api"""

from fortigate_api.api import FortigateAPI
from fortigate_api.fortigate import Fortigate

__all__ = [
    "FortigateAPI",
    "Fortigate",
]

__version__ = "0.1.2"
__date__ = "2022-05-02"
__title__ = "fortigate-api"

__summary__ = "Python package to configure Fortigate (Fortios) devices using REST API"
__author__ = "Vladimir Prusakov"
__email__ = "vladimir.prusakovs@gmail.com"
__url__ = "https://github.com/vladimirs-git/fortigate-api"
__license__ = "MIT"
