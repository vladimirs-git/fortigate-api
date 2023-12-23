"""Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

project = "fortigate-api"
copyright = "2021, Vladimirs Prusakovs"
author = "Vladimirs Prusakovs"
release = "1.3.2"

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
