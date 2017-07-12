# -*- coding: utf-8 -*-
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl).

from __future__ import print_function
import click
import sys
import os
from git import Repo
from git.exc import InvalidGitRepositoryError


@click.command()
@click.argument('path')
def init(path):
    """
    Initialize the structure for file in the git repository

    :param path: The path must be exists, if not it failed
    :type path: str
    :return: exit value from the system, 0 when successfull
    :rtype: int
    """
    if path == '.':
        path = os.getcwd()
    path = os.path.expanduser(path)

    click.echo('Initialise Hosting Configuration in %s' % path)

    # Check if repo contain is a git folder
    try:
        repo = Repo(path)
        print(repo)
    except InvalidGitRepositoryError:
        click.echo('%s Not a valid repository' % path)
        sys.exit(1)

    return sys.exit(0)
