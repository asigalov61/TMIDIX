# docs/conf.py

project = "TMIDIX"
author = "Alex Lev"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx_rtd_theme",
]

autosummary_generate = True

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
