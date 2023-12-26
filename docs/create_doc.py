"""Create documentation sections."""
import logging
from pathlib import Path

from jinja2 import Template
from vhelpers import vre

import fortigate_api
from fortigate_api import FortigateAPI
from fortigate_api import helpers as h
from fortigate_api.types_ import LStr

API = FortigateAPI(host="host")
URL_REPO = "https://github.com/vladimirs-git/fortigate-api"
URL_EXAMPLES = f"{URL_REPO}/tree/main/examples"


# noinspection PyProtectedMember
def create_fortigate_api() -> None:
    """Create FortigateAPI.rst."""
    content_j2 = Path("templates/fortigate_api.j2").read_text()
    class_ = FortigateAPI.__name__
    connectors = FortigateAPI(host="host")._get_connectors()

    text = Template(content_j2).render(
        package=fortigate_api.__name__,
        class_=class_,
        connectors=connectors,
    )
    path = Path(f"{class_}.rst")
    path.write_text(text)
    logging.info("Created %s.", path)


# noinspection PyProtectedMember
def create_connectors() -> None:
    """Create objects/{connector}.rst, where {connector}: Address, AddressGroup, etc."""
    content_j2 = Path("templates/connector.j2").read_text()
    connectors: LStr = API._get_connectors()

    for connector in connectors:
        example = _python_example(connector)
        class_ = h.attr_to_class(connector)

        text = Template(content_j2).render(
            package=fortigate_api.__name__,
            connector=connector,
            class_=class_,
            example=example,
        )

        path = Path("objects", f"{class_}.rst")
        path.write_text(text)
        logging.info("Created %s.", path)


# noinspection PyProtectedMember
def create_objects() -> None:
    """Create objects.rst"""
    content_j2 = Path("templates/objects.j2").read_text()
    connectors: LStr = API._get_connectors()

    items = []
    for connector in connectors:
        connector_o = getattr(API, connector)
        class_ = connector_o.__class__.__name__
        docstring = connector_o.__doc__
        url_ui = vre.find1(r"Web UI:\s+(\S+)", docstring)
        url_api = vre.find1(r"API:\s+(\S+)", docstring)
        example = _url_to_example(connector)

        item = dict(class_=class_, url_ui=url_ui, url_api=url_api, example=example)
        items.append(item)

    text = Template(content_j2).render(items=items)
    path = Path(f"objects.rst")
    path.write_text(text)
    logging.info("Created %s.", path)


def _url_to_example(connector: str) -> str:
    """Return URL to usage example."""
    root = Path(__file__).parent.parent
    path = Path(root, "examples", f"{connector}.py")

    url = ""
    if path.exists():
        url = f"{URL_EXAMPLES}/{connector}.py"
    return url


def _python_example(connector: str) -> str:
    """Return python code wrapped to rst block.

     If file with example does not exist, return empty string.

    :param connector: Connector name.
    :return: Wrapped python code if file exists.
    """
    root = Path(__file__).parent.parent
    path = Path(root, "examples", f"{connector}.py")
    if not path.exists():
        return ""

    text = path.read_text()
    lines = [
        "Usage",
        "-----",
        f"{URL_EXAMPLES}/{connector}.py",
        "",
        ".. code:: python",
        "",
        *[f"    {s}" for s in text.splitlines()],
        "",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler())

    create_fortigate_api()
    create_connectors()
    create_objects()
