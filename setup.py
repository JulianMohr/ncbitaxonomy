# -*- coding: utf-8 -*-

# ! /usr/bin/env python
import os

HERE = os.path.abspath(os.path.split(os.path.realpath(__file__))[0])

from setuptools import setup, find_packages

PYTHON_DEPENDENCIES = [
    # ["numpy", "Numpy is required for the ArrayTable and ClusterTree classes.", 0],
    # ["PyQt", "PyQt4/5 is required for tree visualization and image rendering.", 0],
    # ["lxml", "lxml is required from Nexml and Phyloxml support.", 0]
]

CLASSIFIERS = [
    "Development Status :: 6 - Mature",
    "Environment :: Console",
    "Environment :: X11 Applications :: Qt",
    "Intended Audience :: Developers",
    "Intended Audience :: Other Audience",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "Natural Language :: English",
    "Operating System :: MacOS",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python",
    "Topic :: Scientific/Engineering :: Bio-Informatics",
    "Topic :: Scientific/Engineering :: Visualization",
    "Topic :: Software Development :: Libraries :: Python Modules",
]


# def can_import(mname):
#     'Test if a module can be imported '
#     if mname == "PyQt":
#         try:
#             __import__("PyQt4.QtCore")
#             __import__("PyQt4.QtGui")
#         except ImportError:
#             try:
#                 __import__("PyQt5.QtCore")
#                 __import__("PyQt5.QtGui")
#             except ImportError:
#                 return False
#             else:
#                 return True
#         else:
#             return True
#     else:
#         try:
#             __import__(mname)
#         except ImportError:
#             return False
#         else:
#             return True


try:
    ETE_VERSION = open(os.path.join(HERE, "VERSION")).readline().strip()
except IOError:
    ETE_VERSION = '3.1.2'

print("\nInstalling ncbitaxonomy (cut down ETE) (%s) \n" % ETE_VERSION)
print()

MOD_NAME = "ncbitaxonomy"

LONG_DESCRIPTION = """
This library is a cut down version of ETE3 containing only code that 
is required to run the ncbi_taxnomy module. For full information about 
ETE3 please see http://etetoolkit.org for more info.

The Environment for Tree Exploration (ETE) is a Python programming
toolkit that assists in the recontruction, manipulation, analysis and
visualization of phylogenetic trees (although clustering trees or any
other tree-like data structure are also supported).

ETE is currently developed as a tool for researchers working in
phylogenetics and genomics. If you use ETE for a published work,
please cite:

::

   Jaime Huerta-Cepas, François Serra and Peer Bork. "ETE 3: Reconstruction,
   analysis and visualization of phylogenomic data."  Mol Biol Evol (2016) doi:
   10.1093/molbev/msw046

Visit http://etetoolkit.org for more info.
"""

try:
    _s = setup(
        include_package_data=True,

        name=MOD_NAME,
        version=ETE_VERSION,
        packages=["ncbitaxonomy"],

        entry_points={},
        # Project uses reStructuredText, so ensure that the docutils get
        # installed or upgraded on the target machine
        install_requires=[
        ],
        package_data={

        },
        # metadata for upload to PyPI
        author="cwright",
        author_email="cwright@nanoporetech.com",
        maintainer="Chris Wright",
        maintainer_email="cwright@nanoporetech.com",
        platforms="OS Independent",
        license="GPLv3",
        description="A Python Environment for (phylogenetic) Tree Exploration (Light version)",
        long_description=LONG_DESCRIPTION,
        classifiers=CLASSIFIERS,
        provides=[MOD_NAME],
        keywords="tree, tree reconstruction, tree visualization, tree comparison, phylogeny, phylogenetics, phylogenomics",
        url="http://etetoolkit.org",
        download_url="http://etetoolkit.org/static/releases/ete3/",

    )

except:
    print("\033[91m - Errors found! - \033[0m")
    raise

else:

    print("\033[92m - Done! - \033[0m")
    missing = False
    # for mname, msg, ex in PYTHON_DEPENDENCIES:
    #     if not can_import(mname):
    #         print(" Warning:\033[93m Optional library [%s] could not be found \033[0m" % mname)
    #         print("  ", msg)
    #         missing = True

    notwanted = set(["-h", "--help", "-n", "--dry-run"])
    seen = set(_s.script_args)
    wanted = set(["install", "bdist", "bdist_egg"])
