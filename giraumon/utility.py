# -*- coding: utf-8 -*-
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl).

import os
import shutil
import json
from git import Repo
from git.exc import InvalidGitRepositoryError
from .__about__ import __version__
from giraumon import logger

MANIFEST_FILE = 'manifest.json'

MANIFEST = {
    "name": "My Apps Title",
    "description": """Multi lines description""",
    "website": "http://",
    "repository": "http://",
    "logo": "logo.png",
    "giraumon_version": __version__,
    "success_url": "/success",
    "media_url": {},
    "env": {},
    "templates": [],
}


def create_manifest(path=''):
    """
    Manifest is a JSON file, localte at .platform by default
    We can found it also at the root path
    """
    if not path:
        return False

    pfdir = os.path.join(path, '.platform')
    if not os.path.lexists(pfdir):
        os.mkdir(pfdir)

    mf = os.path.join(path, '.platform', MANIFEST_FILE)
    if not os.path.lexists(mf):
        write_manifest(path, MANIFEST)

    return True


def create_folder(path='', gitkeep=False):
    """
    Create a folder in the location given, if gitkeep parameter
    is true, we add an empty file in this folder, to be Git compatible
    """
    if not os.path.lexists(path):
        os.mkdir(path)
    if gitkeep:
        git_file = os.path.join(path, '.gitkeep')
        with open(git_file, 'w') as fd:
            fd.write('# This is unused, only for git compatibility')

    return True


def find_git_root(path='.'):
    """
    Detect if the current directory is in a git tree
    Return the root git directory
    """
    try:
        if path == '.':
            path = os.getcwd()
        repo = Repo(path)
        return repo.working_dir
    except InvalidGitRepositoryError:
        logger.error('%s Not a valid repository' % os.getcwd())
        return False


def check_manifest(path):
    """
    Check if the current repository have a manifest.json
    in the .platform folder
    """
    pfdir = os.path.join(path, '.platform', MANIFEST_FILE)
    return os.path.exists(pfdir)


def read_manifest(path):
    """
    Read the manifest and return a dict
    """
    mf = os.path.join(path, '.platform', MANIFEST_FILE)
    return json.load(open(mf, 'r'))


def write_manifest(path, content):
    """
    Write the manifest content to the manifest.json
    """
    mf = os.path.join(path, '.platform', MANIFEST_FILE)
    with open(mf, 'w') as fd:
        fd.write(json.dumps(content, indent=2, sort_keys=True))
    return True


def add_template(path, filename):
    """
    Save the template in the .platform/templates
    directory and add extension j2 for Jinja2
    """
    # Retrieve only the filename of the original file
    dest_filename = filename.split(os.sep)[-1]
    tpl = os.path.join(path, '.platform', 'templates', dest_filename + '.j2')
    shutil.copyfile(filename, tpl)
    mf_data = read_manifest(path)
    # Check if this template already in a manifest
    for d in mf_data.get('templates', []):
        if dest_filename in d.get('source', ''):
            break
    else:
        mf_data['templates'].append({
            'source': dest_filename,
            'destination': '',
            'chmod': '600',
        })
        write_manifest(path, mf_data)
