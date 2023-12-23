"""Create documentation sections."""
import logging
from pathlib import Path

from jinja2 import Template

from fortigate_api import FortigateAPI
from fortigate_api.types_ import LStr


# noinspection PyProtectedMember
def create_connectors() -> None:
    """Create api/{class_name}.rst files for connectors."""
    connectors: LStr = FortigateAPI(host="host")._get_connectors()
    content_j2 = Path("connector.j2").read_text()
    template = Template(content_j2)

    for name in connectors:
        obj_name = "".join([s.capitalize() for s in name.split("_")])
        underline = "=" * len(obj_name)
        text = template.render(name=name, obj_name=obj_name, underline=underline)

        path = Path("objects", f"{obj_name}.rst")
        path.write_text(text)
        logging.info("created %s", path)


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler())

    create_connectors()
