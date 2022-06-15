"""fortigate-api"""

from fortigate_api.fortigate import Fortigate
from fortigate_api.fortigate_api import FortigateAPI

__all__ = [
    "Fortigate",
    "FortigateAPI",
]

__version__ = "0.2.4"
__date__ = "2022-06-15"
__title__ = "fortigate-api"

__summary__ = "Python package to configure Fortigate (Fortios) devices using REST API"
__author__ = "Vladimir Prusakov"
__email__ = "vladimir.prusakovs@gmail.com"
__url__ = "https://github.com/vladimirs-git/fortigate-api"
__download_url__ = f"{__url__}/archive/refs/tags/{__version__}.tar.gz"
__license__ = "MIT"
