# -*- coding: utf-8 -*-
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl).
from giraumon.utility import (
    create_manifest, write_manifest, create_folder,
    MANIFEST)
import tempfile
import os


def test_create_manifest_with_no_path():
    assert not create_manifest('')


def test_create_manifest_with_path():
    tpf = tempfile.mkdtemp(prefix='giraumon')
    assert create_manifest(tpf)

def test_write_manifest_with_path():
    tpf = tempfile.mkdtemp(prefix='giraumon')
    assert create_folder(os.path.join(tpf, '.platform'))
    assert write_manifest(tpf, MANIFEST)

