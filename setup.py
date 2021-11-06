"""Package setup"""

import os
from distutils.core import setup

VERSION = os.environ.get("CI_COMMIT_TAG", "0.0.1")
PACKAGE = "fortigate-api"
PACKAGE_ = "fortigate_api"
URL = "https://github.com/vladimirs-git"
DOWNLOAD_URL = f"{URL}/archive/refs/tags/{VERSION}.tar.gz"

if __name__ == '__main__':
    setup(
        name=PACKAGE_,
        packages=[PACKAGE_],
        version=VERSION,
        license="MIT",
        description="Fortigate API",
        author="Vladimir Prusakov",
        author_email="vprusakovs@evolution.com",
        url=f"{URL}/{PACKAGE}",
        download_url=DOWNLOAD_URL,
        keywords=["fortigate", "api", "fortios"],
        install_requires=["requests"],
        classifiers=[
            # How mature is this project? Common values are
            #   3 - Alpha
            #   4 - Beta
            #   5 - Production/Stable
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Build Tools",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.8",
        ],
    )
