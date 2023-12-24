"""Create documentation sections."""
import logging
from pathlib import Path

from jinja2 import Template

import fortigate_api
from fortigate_api import FortigateAPI
from fortigate_api.types_ import LStr

PACKAGE = fortigate_api.__name__


# noinspection PyProtectedMember
def create_fortigate_api() -> None:
    """Create FortigateAPI.rst."""
    content_j2 = Path("templates/fortigate_api.j2").read_text()
    obj = FortigateAPI.__name__
    connectors = FortigateAPI(host="host")._get_connectors()

    text = Template(content_j2).render(
        package=PACKAGE,
        obj=obj,
        connectors=connectors,
        underline="=" * len(obj),
    )
    path = Path(f"{obj}.rst")
    path.write_text(text)
    logging.info("created %s", path)


# noinspection PyProtectedMember
def create_connectors() -> None:
    """Create objects/{connector}.rst, where {connector}: Address, AddressGroup, etc."""
    content_j2 = Path("templates/connector.j2").read_text()
    connectors: LStr = FortigateAPI(host="host")._get_connectors()

    for connector in connectors:
        obj = "".join([s.capitalize() for s in connector.split("_")])
        text = Template(content_j2).render(
            package=PACKAGE,
            connector=connector,
            obj=obj,
            underline="=" * len(obj),
        )

        path = Path("objects", f"{obj}.rst")
        path.write_text(text)
        logging.info("created %s", path)


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler())

    create_fortigate_api()
    create_connectors()
