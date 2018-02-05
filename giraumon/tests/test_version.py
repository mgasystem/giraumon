# -*- coding: utf-8 -*-
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl).
from giraumon.version import version


def test_check_version():
    assert __version__ is not None


