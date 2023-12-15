from setuptools import find_packages, setup

setup(
    name='gendoc',
    version='0.0.1',
    author="QuantifiedCarbon",
    description="gendoc",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(where='src'),
    install_requires=[
        "sphinx",
        "sphinx_rtd_theme",
    ],
)
