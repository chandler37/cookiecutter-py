# -*- coding: utf-8 -*-

"""{{cookiecutter.project_slug}}.{{cookiecutter.project_slug}}: provides entry point main()."""


__version__ = "0.1.0"

import argparse
import sys

from .cat import read_file_lines


class Error(Exception):
    """It is good practice to define an Error class that is the
    superclass of all exceptions defined in a module. This is it.
    """


class UsageError(Error):
    """You invoked the program with invalid arguments."""


def cat_cmd(args):
    try:
        read_file_lines(args.path)
    except IOError:
        raise UsageError(
            'Needs a path to an existing file; {} does not exist or cannot be read'.format(args.path))


def main():
    try:
        parser = argparse.ArgumentParser(
            prog='{{cookiecutter.project_slug}}',
            description="""A smorgasbord of pythonic goodness. We're learning as we go.

Remember that the pseudoargument "--" causes all following arguments to become
positional arguments (as opposed to flags)""")

        parser.add_argument(
            '--version', action='version', version='%(prog)s {}'.format(__version__))
        subparsers = parser.add_subparsers(help='TODO: sub-command help')

        parser_cat = subparsers.add_parser(
            'cat',
            help='reads a file line by line and prints each line (does not preserve trailing whitespace)')
        parser_cat.add_argument(
            'path',
            help='path (absolute or relative) to an existing, readable file')
        parser_cat.set_defaults(func=cat_cmd)

        args = parser.parse_args()
        if not hasattr(args, 'func'):
            # According to https://mail.python.org/pipermail/python-dev/2017-December/151283.html, in python 3.7 or
            # later, the order is guaranteed to be the same as the order in the source code above (because choices is a
            # dict):
            choices = ', '.join(subparsers.choices.keys())
            raise UsageError(
                "A subcommand must be provided from the following list: {}".format(choices))
        args.func(args)
    except UsageError as e:
        print('Usage error: {}'.format(str(e)))
        sys.exit(1)
