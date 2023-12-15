import os
import subprocess

def doc_python(name_project, dir_input):
    print('--- generating python docs ---')

    os.makedirs('sphinx')
    os.chdir('sphinx')

    name_author = 'QuantifiedCarbon'

    config_conf = f'''import os
import sys
sys.path.insert(0, os.path.abspath("../../{dir_input}")) 
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",    
]'''

    config_index = f'''.. {name_project} documentation master file, created by
    sphinx-quickstart on Thu Dec 14 02:41:16 2023.
    You can adapt this file completely to your liking, but it should at least
    contain the root `toctree` directive.

{name_project} documentation
=================================

.. toctree::
    :maxdepth: 2
    :caption: Contents:

    modules


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
'''

    theme_conf = 'html_theme = "sphinx_rtd_theme"'

    print('creating sphinx-quickstart')
    process = subprocess.Popen('sphinx-quickstart', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    stdout, _ = process.communicate(input=f'\n{name_project}\n{name_author}\n\n\n')

    print('configurating conf.py and index.rst')
    with open('conf.py', 'r') as f: file = f.read().split('\n')
    config_conf = config_conf.split('\n')

    for i, line in enumerate(file):
        if 'extensions = ' in line:
            file = file[:i] + config_conf + file[i + 1:]
            break

    for i, line in enumerate(file):
        if 'html_theme = ' in line:
            file[i] = theme_conf
            break

    file = '\n'.join(file)
    with open('conf.py', 'w') as f: f.write(file)

    file = config_index
    with open('index.rst', 'w') as f: f.write(file)

    print('generating rst files')
    process = subprocess.Popen(f'sphinx-apidoc -o . ../../{dir_input}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    process.wait()

    print('making html files')
    process = subprocess.Popen('.\\make html', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    process.wait()
    
    os.chdir('..')

    print('--- python docs created ---')

def doc_cpp(name_project, dir_input):
    print('--- generating c++ docs ---')

    os.makedirs('doxygen')
    os.chdir('doxygen')

    config_doxyfile = f'''PROJECT_NAME           = "{name_project}"
INPUT                  = "../../{dir_input}"
OUTPUT_DIRECTORY       = "."
RECURSIVE              = YES
VERBATIM_HEADERS       = NO
GENERATE_HTML          = YES
GENERATE_LATEX         = NO'''

    print('creating doxygen file')
    process = subprocess.Popen('doxygen -g', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    process.wait()

    print('configurating Doxyfile')
    with open('Doxyfile', 'r') as f: file = f.read().split('\n')
    config_doxyfile = config_doxyfile.split('\n')

    for config in config_doxyfile:
        for i, line in enumerate(file):
            if config.split('=')[0] in line:
                file[i] = config

    file = '\n'.join(file)
    with open('Doxyfile', 'w') as f: f.write(file)

    print('making html files')
    process = subprocess.Popen('doxygen Doxyfile', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    os.chdir('..')

    print('--- c++ docs created ---')