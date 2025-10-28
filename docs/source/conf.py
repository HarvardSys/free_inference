"""Sphinx configuration for the Free Inference user documentation.

This module configures Sphinx extensions, HTML theme, and source parsers
used to build the user-facing documentation. This documentation focuses
on helping users get started and use the Free Inference API.
"""

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# Add project root to sys.path for autodoc
sys.path.insert(0, os.path.abspath("../.."))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Free Inference"
copyright = "2025, Harvard System Lab"
author = "Harvard System Lab"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",  # Support for Markdown files
    "sphinx.ext.intersphinx",  # Link to other project's documentation
]

# MyST parser configuration
myst_enable_extensions = [
    "colon_fence",  # ::: fences
    "deflist",  # Definition lists
    "tasklist",  # Task lists
]

# Intersphinx mapping - link to Python docs for better references
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

templates_path = ["_templates"]
exclude_patterns = []

# Source file suffixes
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# RTD theme options
html_theme_options = {
    "navigation_depth": 4,
    "collapse_navigation": False,
    "sticky_navigation": True,
    "includehidden": True,
    "titles_only": False,
}

# Custom CSS files
html_css_files = [
    "custom.css",
]

# Add .nojekyll file for GitHub Pages to prevent Jekyll processing
# This ensures _static and other underscore-prefixed folders are served correctly
html_extra_path = []


def setup(app):
    """Sphinx setup hook to create .nojekyll file for GitHub Pages."""
    import os

    def create_nojekyll(app, exception):
        """Create .nojekyll file in build output directory."""
        if exception is None and app.builder.name == 'html':
            nojekyll_path = os.path.join(app.outdir, '.nojekyll')
            with open(nojekyll_path, 'w') as f:
                pass  # Create empty file

    app.connect('build-finished', create_nojekyll)

