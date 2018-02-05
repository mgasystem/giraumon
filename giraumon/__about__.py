# -*- coding: utf-8 -*-
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl).
from __future__ import absolute_import, division, print_function
from pkg_resources import get_distribution, DistributionNotFound

__all__ = [
    "__title__", "__summary__", "__uri__", "__version__", "__author__",
    "__email__", "__license__", "__copyright__",
]

__title__ = "giraumon"
__summary__ = "Tools to prepare deployment"
__uri__ = "https://github.com/mgasystem/giraumon"

__author__ = "Christophe CHAUVET"
__email__ = "christophe.chauvet@gmail.com"

__license__ = "GPLv3"
__copyright__ = "Copyright 2016-2017 %s" % __author__

try:
    __version__ = get_distribution('giraumon').version
except DistributionNotFound:
    # package is not installed
    pass  # noqa
