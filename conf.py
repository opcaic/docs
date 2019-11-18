# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'OPCAIC'
copyright = '2019, OPCAIC Team'
author = 'OPCAIC Team'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'recommonmark',
    'sphinx.ext.todo',
    'sphinxcontrib.inkscapeconverter',
]

source_suffix = ['.rst', '.md']

master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['#*', 'readme.md', '_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_context = {
    'css_files': [
        '_static/theme_overrides.css' # override for wide tables
    ]
}

# -- Options for LaTeX output -------------------------------------------------

latex_additional_files = [
    '_templates/styleoverrides.sty',
    '_templates/title.tex.txt'
]

latex_show_urls = 'footnote'

latex_show_pagerefs = True

latex_documents = [
    (master_doc, 'doc.tex', 'Online Platform for Conducting AI Tournaments',
      r'''Radek Zikmund \and \\
      Ondřej Nepožitek \and \\
      Michal Lehončák \and \\
      Šimon Stachura''', 'manual') 
]

latex_elements = {
    'figure_align': 'H',

    'papersize': 'a4paper',
    
    'maketitle': r'''
        \pagenumbering{Roman} %%% to avoid page 1 conflict with actual page 1

        \begin{titlepage}
            \centering

            \vspace*{60mm} %%% * is used to give space from top
            \textbf{\Huge {OPCAIC}}

            \vspace{20mm}

            \textbf{\huge {Online Platform for Conducting AI Tournaments}}

            \vspace{60mm}
            {\Large
                Bc. Radek Zikmund,

                Bc. Ondřej Nepožitek,

                Bc. Michal Lehončák,

                Bc. Šimon Stachura
            }


            \vspace*{20mm}
            \small  \MonthYearFormat\today


            %% \vfill adds at the bottom
            %% \vfill
        \end{titlepage}

        \cleardoublepage
        \pagenumbering{roman}

        \include{title.tex.txt}
    ''',

    'preamble': r'''
        \usepackage[ddmmyy]{datetime}
        \usepackage{svg}
        \newdateformat{MonthYearFormat}{%
                    \monthname[\THEMONTH], \THEYEAR}
        \usepackage{styleoverrides}
        \addto\captionsenglish{\renewcommand{\contentsname}{Table of contents}}
        
        % make counters behave sanely
        \counterwithin{figure}{chapter}
        \counterwithin{literalblock}{chapter}

        \def\chapwithtoc#1{
        \chapter*{#1}
        \addcontentsline{toc}{chapter}{#1}
        }
    '''
}

todo_include_todos = True
