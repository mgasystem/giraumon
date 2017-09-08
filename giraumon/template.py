# -*- coding: utf-8 -*-
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl).

from __future__ import print_function
import click
import sys

from giraumon import logger
from .utility import find_git_root, check_manifest, add_template


@click.command()
@click.option('-a', '--add', type=click.Path(
    exists=True, file_okay=True, readable=True, resolve_path=True))
@click.option('-r', '--render', type=click.Path(
    exists=True, file_okay=True, readable=True, resolve_path=True))
@click.argument('path', type=click.Path())
def template(add, render, path):
    """
    Add option: Copy template to the folder template
    Render: take template and render it
    """

    wk_dir = find_git_root(path)
    if not wk_dir:
        logger.error('No git repository found !')
        return sys.exit(1)

    logger.info('Working directory %s' % wk_dir)
    if not check_manifest(wk_dir):
        logger.error('No manifest file found !')
        return sys.exit(1)

    if add is not None:
        add_template(wk_dir, add)

    return sys.exit(0)
