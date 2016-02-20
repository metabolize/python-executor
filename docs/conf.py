"""
Documentation build configuration file for the `executor` package.

This Python script contains the Sphinx configuration for building the
documentation of the `executor` project. This file is execfile()d with
the current directory set to its containing dir.
"""

import os
import sys
import types

# Add the 'executor' source distribution's root directory to the module path.
sys.path.insert(0, os.path.abspath(os.pardir))

# -- General configuration -----------------------------------------------------

# Sphinx extension module names.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'humanfriendly.sphinx',
]

# Paths that contain templates, relative to this directory.
templates_path = ['templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'executor'
copyright = u'2016, Peter Odding'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# Find the package version and make it the release.
from executor import __version__ as executor_version

# The short X.Y version.
version = '.'.join(executor_version.split('.')[:2])

# The full version, including alpha/beta/rc tags.
release = executor_version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['build']

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Refer to the Python standard library.
# From: http://twistedmatrix.com/trac/ticket/4582.
intersphinx_mapping = dict(
    python2=('http://docs.python.org', None),
    python3=('http://docs.python.org/3', None),
    humanfriendly=('https://humanfriendly.readthedocs.org/en/latest', None),
    propertymanager=('https://property-manager.readthedocs.org/en/latest', None),
)

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'

# Output file base name for HTML help builder.
htmlhelp_basename = 'executordoc'

# -- Customizations of the autodoc plug-in -------------------------------------

# Sort members by the source order instead of alphabetically.
autodoc_member_order = 'bysource'
