import click.testing
import pytest

@pytest.fixture
def runner():
    return click.testing.CliRunner()

from wikiapp import console

def test_main_succeeds(runner):
    result = runner.invoke(console.main)
    assert result.exit_code == 0
