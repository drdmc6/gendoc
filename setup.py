from setuptools import find_packages, setup
import os

setup(
    name='gendoc',
    version='0.1',
    author="QuantifiedCarbon",
    packages=find_packages(),
    install_requires=[
        "sphinx",
        "sphinx_rtd_theme",
    ],
)
