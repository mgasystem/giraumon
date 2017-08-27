# -*- coding: utf-8 -*-
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl).

from click.testing import CliRunner
from giraumon.template import template


def test_template_without_options():
    """Test template on folder with no git root"""
    runner = CliRunner()
    result = runner.invoke(template, [])
    assert result.exit_code == 0


def test_template_with_add_options_empty():
    """Test template on folder with no git root"""
    runner = CliRunner()
    result = runner.invoke(template, ['--add'])
    assert result.exit_code == 2


def test_template_with_add_options():
    """Test template on folder with no git root"""
    runner = CliRunner()
    result = runner.invoke(template, ['--add', '/etc/hosts'])
    assert result.exit_code == 0
