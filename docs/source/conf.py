# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import re

sys.path.insert(0, os.path.abspath('exts'))

MSG_DIR = os.environ['MSG_DIR']
sys.path.insert(0, os.path.join(MSG_DIR, 'python'))

import sphinx_rtd_theme


# -- Project information -----------------------------------------------------

project = 'MSG'
author = 'Rich Townsend & The MSG Team'
version = "main"
release = "main"
branch = "main"
copyright = '2021, Rich Townsend & The MSG Team'


# -- General configuration ---------------------------------------------------

# Numbered figures
numfig = True

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.mathjax',
    'sphinx.ext.extlinks', 
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx-prompt',
    'sphinx_substitution_extensions',
    'nbsphinx',
    'ads_cite',
    'sphinxfortran.fortran_domain'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Additional configuration ------------------------------------------------

# sphinx_rtd options
html_theme_options = {
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
    'logo_only': True
}

# CSS
#html_context = {
#    'css_files': [
#        '_static/theme_overrides.css'  # override wide tables in RTD theme
#    ],
#}

# Set master doc
master_doc = 'index'

# Set logo
html_logo = 'msg-logo.png'

# Set up Extlinks
extlinks = {
    'wiki': ('https://en.wikipedia.org/wiki/%s', ''),
    'ads': ('https://ui.adsabs.harvard.edu/abs/%s/abstract', ''),
    'netlib': ('https://www.netlib.org/%s', ''),
    'git': ('https://github.com/%s', ''),
    'repo': ('https://github.com/rhdtownsend/msg/blob/{:s}/%s'.format(branch), ''),
    'grids': ('http://www.astro.wisc.edu/~townsend/resource/download/msg/grids/%s', ''),
    'passbands': ('http://www.astro.wisc.edu/~townsend/resource/download/msg/passbands/%s', '')
}

# Set site-wide targets

if release == 'main':
    tarball = 'main'
else:
    tarball = 'v{0:s}'.format(release)

targets = {
    'github-tarball': 'https://api.github.com/repos/rhdtownsend/msg/tarball/{0:s}'.format(tarball),
    'madstar-tarball': 'http://www.astro.wisc.edu/~townsend/resource/download/software/msg-main.tar.gz',
    'mesa-sdk': 'http://www.astro.wisc.edu/~townsend/static.php?ref=mesasdk',
    'mesa': 'http://mesa.sourceforge.net/',
}

rst_prolog = '\n'.join(['.. _{:s}: {:s}'.format(x, targets[x]) for x in targets])

# Add substitutions for sphinx_substitution_extensions

rep_exts = {"release": release,
            "author": author}

for rep_ext_key, rep_ext_val in rep_exts.items():
    rst_prolog += "\n.. |{:s}| replace:: {:s}".format(rep_ext_key, rep_ext_val)

# Mathjax & Latex macros

macros = {}

with open('macros.def', encoding='utf-8') as f:
    line = f.readline()
    while line:
        key, value = line.rstrip().split('\t')
        macros[key] = value
        line = f.readline()

mathjax_macros = {}

for key, value in macros.items():
    argnums = re.findall('#(\d)', value)
    if argnums:
        mathjax_macros[key] = [value, int(max(argnums))]
    else:
        mathjax_macros[key] = value

#mathjax_config = {                  
#    'TeX': { 
#        'Macros': mathjax_macros
#    }
#}
mathjax3_config = {                  
    'tex': { 
        'macros': mathjax_macros
    }
}

# Enable email obfuscation
email_automode = True

# Set up intersphinx
intersphinx_mapping = {
    'numpy': ('http://docs.scipy.org/doc/numpy/', None),
    'matplotlib': ('https://matplotlib.org/stable/', None)
}

# Set up autodoc
autoclass_content = 'class'
autodoc_member_order = 'groupwise'

# Set up napoleon
napoleon_google_docstring = True
napoleon_include_init_with_doc = True

# Set up nbsphinx
nbsphinx_execute = 'never'
