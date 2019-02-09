# -*- coding: utf-8 -*-
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl).

from __future__ import print_function
import click
import sys

from . import __version__ as version
from .initialize import init
from .template import template
from giraumon import logger


@click.group()
def cli():
    """Entry point for the global management tools"""
    click.clear()  # pragma: no cover
    logger.info('Giraumon Tools version: %s' % version)  # pragma: no cover
    logger.info('- Platform: %s' % sys.platform)  # pragma: no cover
    logger.info('- Python version: %s' % sys.version)  # pragma: no cover


cli.add_command(init)
cli.add_command(template)
