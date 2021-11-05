"""Base settings"""

import os

VERSION = os.environ.get("CI_COMMIT_TAG", "0.0.1")
AUTHOR = "Vladimir Prusakov"
AUTHOR_EMAIL = "vprusakovs@evolution.com"

# OS files, paths
APP_NAME = "fortigate_api"
PACKAGE_DIR = os.path.dirname(os.path.realpath(__file__))
PACKAGE = os.path.split(PACKAGE_DIR)[1]
URL = "https://rms.evolutiongaming.com/evo-pypi/noc"
DOWNLOAD_URL = f"{URL}/archive/refs/tags/{VERSION}.tar.gz"
