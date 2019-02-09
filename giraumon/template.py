# -*- coding: utf-8 -*-
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl).

from __future__ import print_function
import click
import sys

from giraumon import logger
from .utility import find_git_root, check_manifest, add_template


@click.command('template')
def template():
    """
    Manage template with some subcommand
    """

    return sys.exit(0)


@click.command('template:add')
@click.argument('path', type=click.Path())
def template_add(path):
    """
    Copy template to the folder template
    """
    wk_dir = find_git_root(path)
    if not wk_dir:
        logger.error('No git repository found !')
        return sys.exit(1)

    logger.info('Working directory %s' % wk_dir)
    if not check_manifest(wk_dir):
        logger.error('No manifest file found !')
        return sys.exit(1)

    add_template(wk_dir, path)

    return sys.exit(0)
