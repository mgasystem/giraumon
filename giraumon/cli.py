# -*- coding: utf-8 -*-
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl).

from __future__ import print_function
import click

from .initialize import init


@click.group()
def cli():
    """Entry point for the global management tools"""
    pass


cli.add_command(init)
