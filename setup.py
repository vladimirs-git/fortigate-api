"""setup"""

from distutils.core import setup

from fortigate_api import setting


setup(
    name=setting.PACKAGE,
    packages=[setting.PACKAGE],
    version=setting.VERSION,
    license="MIT",
    description="Fortigate API",
    author=setting.AUTHOR,
    author_email=setting.AUTHOR_EMAIL,
    url=f"{setting.URL}/{setting.APP_NAME}",
    download_url=setting.DOWNLOAD_URL,
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
