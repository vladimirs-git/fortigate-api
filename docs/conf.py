"""Configuration file for the Sphinx documentation builder."""

project = "fortigate-api"
copyright = "2021, Vladimirs Prusakovs"
author = "Vladimirs Prusakovs"
release = "1.4.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
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


def process_signature(app, what, name, obj, options, signature, return_annotation):
    """Modify class docstring."""
    _ = f"{app=} {what=} {name=} {obj=} {options=} {signature=} {return_annotation=}"
    # logging.warning(_)
    # if what == "class" and name == "fortigate_api.base.Base":
    #     return "", ""


def process_docstring(app, what, name, obj, options, lines: list):
    """Skip docstrings of class Base, Base.__init__."""
    _ = f"{app=} {what=} {name=} {obj=} {options=} {lines=}"
    # logging.warning(_)
    # if what == "class" and name == "fortigate_api.base.Base":
    #     lines.clear()


def skip(app, what, name, obj, would_skip, options):
    """Modify members docstring."""
    _ = f"{app=} {what=} {name=} {obj=} {would_skip=} {options=}"
    # logging.warning(_)
    return would_skip


def setup(app):
    """Setup."""
    app.connect("autodoc-skip-member", skip)
    app.connect("autodoc-process-signature", process_signature)
    app.connect("autodoc-process-docstring", process_docstring)
