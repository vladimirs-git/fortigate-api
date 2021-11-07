"""Package fortigate-api"""

from fortigate_api.api import FortigateAPI
from fortigate_api.fortigate import Fortigate

__version__ = "0.0.6"
__title__ = "fortigate-api"
__summary__ = "Python package to configure Fortigate (Fortios) devices using REST API"
__author__ = "Vladimir Prusakov"
__email__ = "vprusakovs@evolution.com"
__url__ = "https://rms.evolutiongaming.com/evo-pypi/noc"
__download_url__ = f"{__url__}/{__title__}-{__version__}.tar.gz"
__project_urls__ = {"fw-rules-app": "https://gitlab.evolutiongaming.com/noc/pan/fw-rules-app"}
__license__ = "MIT"
