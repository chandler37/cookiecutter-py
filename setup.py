# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('{{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}.py').read(),
    re.M
    ).group(1)


with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "cmdline-{{cookiecutter.project_slug}}",
    packages = ["{{cookiecutter.project_slug}}"],
    entry_points = {
        "console_scripts": ['{{cookiecutter.project_slug}} = {{cookiecutter.project_slug}}.{{cookiecutter.project_slug}}:main']
        },
    version = version,
    description = "Python command line application {{cookiecutter.project_slug}}.",
    long_description = long_descr
    )
