# -*- coding: utf-8 -*-
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl).

from click.testing import CliRunner
from giraumon.initialize import init


def test_init_without_repo():
    """Test init with forlder with no git root """
    runner = CliRunner()
    result = runner.invoke(init, ['.'])
    assert not result.exception

