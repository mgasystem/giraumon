# -*- coding: utf-8 -*-
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl).
from giraumon import logger


def test_logger_info():
    output = logger.info('Test')
    assert output is None


def test_logger_warn():
    output = logger.warn('Test')
    assert output is None


def test_logger_error():
    output = logger.error('Test')
    assert output is None
