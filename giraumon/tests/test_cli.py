# -*- coding: utf-8 -*-
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl).

from click.testing import CliRunner
from giraumon.cli import cli


def test_cli_without_argument():
    """When there are no argument, cli must failed"""

    runner = CliRunner()
    result = runner.invoke(cli, [])
    assert not result.exception
