"""Configuration file for the Sphinx documentation builder."""
import logging

from tabulate import tabulate

logging.basicConfig(level=logging.DEBUG)

project = "fortigate-api"
copyright = "2021, Vladimirs Prusakovs"
author = "Vladimirs Prusakovs"
release = "2.0.2"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinxcontrib.httpdomain",
    "sphinxcontrib.openapi",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

master_doc = "index"

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

autoclass_content = "both"

autodoc_default_options = {
    # "members": True,
    "member-order": "bysource",
    # "special-members": "__init__",
    # "undoc-members": True,
    # "exclude-members": "__weakref__"
}

IP = "172.16.177.65"


def skip(app, what, name, obj, would_skip, options):
    """Modify members docstring."""
    _ = f"{app=} {what=} {name=} {obj=} {would_skip=} {options=}"
    # logging.warning(_)
    return would_skip


def process_signature(app, what, name, obj, options, signature, return_annotation):
    """Modify class docstring."""
    _ = f"{app=} {what=} {name=} {obj=} {options=} {signature=} {return_annotation=}"
    # logging.warning(_)
    # if what == "class" and name == "fortigate_api.base.Base":
    #     return "", ""


# noinspection PyProtectedMember
def process_docstring(app, what, name, obj, options, lines: list):
    """Add URL to documentation in docstring."""
    _ = f"{app=} {what=} {name=} {obj=} {options=} {lines=}"
    if what == "class" and name.startswith("fortigate_api."):
        if not (hasattr(obj, "_path_ui") and hasattr(obj, "_path")):
            return

        # Connector docstring
        rows = []
        # url_web
        url_web = ""
        if obj._path_ui:
            url_web = f"https://{IP}/{obj._path_ui}"
        rows.append(("Web UI", url_web))

        # url_api
        url_api = f"https://{IP}/{obj._path}"
        rows.append(("API", url_api))

        # url_data
        url_data = ""
        if obj._path_ui:
            url_data = str(obj._path).replace("api/v2/", "", 1)
            url_data = f":ref:`{url_data}`"
        rows.append(("Data", url_data))

        table = tabulate(rows, headers=[], tablefmt="rst")
        lines.clear()
        lines.extend(table.splitlines())


def setup(app):
    """Setup."""
    app.connect("autodoc-skip-member", skip)
    app.connect("autodoc-process-signature", process_signature)
    app.connect("autodoc-process-docstring", process_docstring)
