"""Package setup"""

import os
import pathlib

from setuptools import setup  # type: ignore

import fortigate_api as packet

PACKAGE = packet.__title__
PACKAGE_ = packet.__title__.lower().replace("-", "_")  # PEP 503 normalization
ROOT = pathlib.Path(__file__).parent.resolve()

if __name__ == "__main__":
    setup(
        name=PACKAGE_,
        packages=[PACKAGE_],
        version=os.environ.get("CI_COMMIT_TAG", packet.__version__),
        license=packet.__license__,
        description=packet.__summary__,
        long_description=(ROOT / "README.md").read_text(encoding="utf-8"),
        long_description_content_type="text/markdown",
        author=packet.__author__,
        author_email=packet.__email__,
        url=packet.__url__,
        download_url=packet.__download_url__,
        keywords="fortigate, api, fortios, firewall, networking, telecommunication",
        python_requires=">=3.8",
        install_requires=["requests"],
        classifiers=[
            # "Development Status :: 3 - Alpha",
            "Development Status :: 4 - Beta",
            # "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "Intended Audience :: System Administrators",
            "Intended Audience :: Telecommunications Industry",
            "Operating System :: FortiOS",
            "Topic :: System :: Networking :: Firewalls",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3.8",
        ],
    )
