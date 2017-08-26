# -*- coding: utf-8 -*-
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl).
from giraumon import logger


def test_logger_info(capsys):
    logger.info('Test')
    out, err = capsys.readouterr()
    assert 'Test' in out


def test_logger_warn(capsys):
    logger.warn('Test')
    out, err = capsys.readouterr()
    assert 'Test' in out


def test_logger_error(capsys):
    logger.error('Test')
    out, err = capsys.readouterr()
    assert 'Test' in out


def test_logger_info_multilines(capsys):
    logger.info('Test1\nTest2\Test3')
    out, err = capsys.readouterr()
    assert 'Test' in out


def test_logger_warn_multilines(capsys):
    logger.warn('Test1\nTest2\Test3')
    out, err = capsys.readouterr()
    assert 'Test' in out


def test_logger_error_multilines(capsys):
    logger.error('Test1\nTest2\Test3')
    out, err = capsys.readouterr()
    assert 'Test' in out
