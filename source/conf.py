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
import os
import sys
sys.path.insert(
    0,
    os.path.abspath(
        '/Users/connor/Google Drive/Documents/University/Courses/2020/ENGSCI 700A&B/GOCPI/src/GOCPI/GOCPI'
    ))

# Add additional paths to create options.
# Source '/Users/connor/Google Drive/Documents/University/Courses/2020/ENGSCI 700A&B/GOCPI/source'
# Modules '/Users/connor/Google Drive/Documents/University/Courses/2020/ENGSCI 700A&B/GOCPI/src/GOCPI/GOCPI'

# sphinx-apidoc -o <OUTPUT_PATH> <MODULE_PATH>
# Command to generate files

# sphinx-apidoc -o '/Users/connor/Google Drive/Documents/University/Courses/2020/ENGSCI 700A&B/GOCPI/source' '/Users/connor/Google Drive/Documents/University/Courses/2020/ENGSCI 700A&B/GOCPI/src/GOCPI/GOCPI'

# Build latex command
# sphinx-build -b latex '/Users/connor/Google Drive/Documents/University/Courses/2020/ENGSCI 700A&B/GOCPI/source' '/Users/connor/Google Drive/Documents/University/Courses/2020/ENGSCI 700A&B/GOCPI/src/GOCPI/GOCPI'

# -- Project information -----------------------------------------------------

project = 'GOCPI'
copyright = '2020, Connor Robert McDowall'
author = 'Connor Robert McDowall'

# The full version, including alpha/beta/rc tags
release = '3.0.9330'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The master toctree document.
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Options for Latex Output
# -- Options for LaTeX output ---------------------------------------------

latex_engine = 'pdflatex'
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'a4paper',
    'releasename':" ",
    # Sonny, Lenny, Glenn, Conny, Rejne, Bjarne and Bjornstrup
    # 'fncychap': '\\usepackage[Lenny]{fncychap}',
    'fncychap': '\\usepackage{fncychap}',
    'fontpkg': '\\usepackage{amsmath,amsfonts,amssymb,amsthm}',

    'figure_align':'htbp',
    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '12pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': r'''
        %%%%%%%%%%%%%%%%%%%% Meher %%%%%%%%%%%%%%%%%%
        %%%add number to subsubsection 2=subsection, 3=subsubsection
        %%% below subsubsection is not good idea.
        \setcounter{secnumdepth}{3}
        %
        %%%% Table of content upto 2=subsection, 3=subsubsection
        \setcounter{tocdepth}{2}

        \usepackage{amsmath,amsfonts,amssymb,amsthm}
        \usepackage{graphicx}

        %%% reduce spaces for Table of contents, figures and tables
        %%% it is used "\addtocontents{toc}{\vskip -1.2cm}" etc. in the document
        \usepackage[notlot,nottoc,notlof]{}

        \usepackage{color}
        \usepackage{transparent}
        \usepackage{eso-pic}
        \usepackage{lipsum}

        \usepackage{footnotebackref} %%link at the footnote to go to the place of footnote in the text

        %% spacing between line
        \usepackage{setspace}
        %%%%\onehalfspacing
        %%%%\doublespacing
        \singlespacing


        %%%%%%%%%%% datetime
        \usepackage{datetime}

        \newdateformat{MonthYearFormat}{%
            \monthname[\THEMONTH], \THEYEAR}


        %% RO, LE will not work for 'oneside' layout.
        %% Change oneside to twoside in document class
        \usepackage{fancyhdr}
        \pagestyle{fancy}
        \fancyhf{}

        %%% Alternating Header for oneside
        \fancyhead[L]{\ifthenelse{\isodd{\value{page}}}{ \small \nouppercase{\leftmark} }{}}
        \fancyhead[R]{\ifthenelse{\isodd{\value{page}}}{}{ \small \nouppercase{\rightmark} }}

        %%% Alternating Header for two side
        %\fancyhead[RO]{\small \nouppercase{\rightmark}}
        %\fancyhead[LE]{\small \nouppercase{\leftmark}}

        %% for oneside: change footer at right side. If you want to use Left and right then use same as header defined above.
        \fancyfoot[R]{\ifthenelse{\isodd{\value{page}}}{{\tiny Meher Krishna Patel} }{\href{http://pythondsp.readthedocs.io/en/latest/pythondsp/toc.html}{\tiny PythonDSP}}}

        %%% Alternating Footer for two side
        %\fancyfoot[RO, RE]{\scriptsize Meher Krishna Patel (mekrip@gmail.com)}

        %%% page number
        \fancyfoot[CO, CE]{\thepage}

        \renewcommand{\headrulewidth}{0.5pt}
        \renewcommand{\footrulewidth}{0.5pt}

        \RequirePackage{tocbibind} %%% comment this to remove page number for following
        \addto\captionsenglish{\renewcommand{\contentsname}{Table of contents}}
        \addto\captionsenglish{\renewcommand{\listfigurename}{List of figures}}
        \addto\captionsenglish{\renewcommand{\listtablename}{List of tables}}
        % \addto\captionsenglish{\renewcommand{\chaptername}{Chapter}}


        %%reduce spacing for itemize
        \usepackage{enumitem}
        \setlist{nosep}

        %%%%%%%%%%% Quote Styles at the top of chapter
        \usepackage{epigraph}
        \setlength{\epigraphwidth}{0.8\columnwidth}
        \newcommand{\chapterquote}[2]{\epigraphhead[60]{\epigraph{\textit{#1}}{\textbf {\textit{--#2}}}}}
        %%%%%%%%%%% Quote for all places except Chapter
        \newcommand{\sectionquote}[2]{{\quote{\textit{``#1''}}{\textbf {\textit{--#2}}}}}
    ''',


    'maketitle': r'''
        \pagenumbering{Roman} %%% to avoid page 1 conflict with actual page 1

        \begin{titlepage}
        \newcommand{\HRule}{\rule{\linewidth}{0.5mm}} % Defines a new command for horizontal lines, change thickness here
        
        \center
        
        %------------------------------------------------
        %	Headings
        %------------------------------------------------
        
        \textsc{\LARGE }\\[1.5cm] % Main heading such as the name of your university/college
        
        \textsc{\Large University of Auckland\\Department of Engineering Science}\\[0.5cm] % Major heading such as course name
        
        %------------------------------------------------
        %	Title
        %------------------------------------------------
        
        \HRule\\[0.5cm]
        
        {\huge\bfseries Global Optimisation Carbon Pricing Initiative (GOCPI) Modules}\\[0.4cm] % Title of your document
        
        \HRule\\[0.5cm]
        
        %------------------------------------------------
        %	Author(s)
        %------------------------------------------------
        
        {\large\textit{Author: Connor McDowall \\Supervisor: Rosalind Archer}}\\
        
        %------------------------------------------------
        %	Date
        %------------------------------------------------
        
        \vfill\vfill\vfill % Position the date 3/4 down the remaining page
        
        {\large\today} % Date, change the \today to a set date if you want to be precise
        
        %----------------------------------------------------------------------------------------
        
        \vfill % Push the date up 1/4 of the remaining page
        
    \end{titlepage}

        \clearpage
        \pagenumbering{roman}
        \tableofcontents
        \listoffigures
        \listoftables
        \clearpage
        \pagenumbering{arabic}

        ''',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
    'sphinxsetup': \
        'hmargin={0.7in,0.7in}, vmargin={1in,1in}, \
        verbatimwithframe=true, \
        TitleColor={rgb}{0,0,0}, \
        HeaderFamily=\\rmfamily\\bfseries, \
        InnerLinkColor={rgb}{0,0,1}, \
        OuterLinkColor={rgb}{0,0,1}'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ,

        'tableofcontents':' ',
}

latex_logo = '_static/logo.jpg'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'GOCPI-appendix.tex', 'GOCPI Sphinx format for Latex ',
     'Connor Robert McDowall', 'article')
]