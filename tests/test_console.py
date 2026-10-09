"""Tests of the command, `main`, run in the same process by click's CliRunner."""

from unittest.mock import Mock

import pytest
import requests
from click.testing import CliRunner

from wikiapp import console


@pytest.fixture
def runner() -> CliRunner:  # A runner that calls a command and keeps what it prints
    """Give each test a runner for the command."""
    return CliRunner()


def test_main_prints_title(
    runner: CliRunner,  # The runner from the fixture
    mock_requests_get: Mock,  # The mock of `requests.get`, from conftest.py
) -> None:
    """The command prints the title of the page."""
    result = runner.invoke(console.main)
    assert "Lorem Ipsum" in result.output


def test_main_invokes_requests_get(
    runner: CliRunner,  # The runner from the fixture
    mock_requests_get: Mock,  # The mock of `requests.get`, from conftest.py
) -> None:
    """The command makes a request."""
    runner.invoke(console.main)
    assert mock_requests_get.called


def test_main_uses_correct_url(
    runner: CliRunner,  # The runner from the fixture
    mock_requests_get: Mock,  # The mock of `requests.get`, from conftest.py
) -> None:
    """The request goes to the random page of the English Wikipedia."""
    runner.invoke(console.main)
    assert mock_requests_get.call_args[0] == (
        "https://en.wikipedia.org/api/rest_v1/page/random/summary",
    )


def test_main_fails_on_request_error(
    runner: CliRunner,  # The runner from the fixture
    mock_requests_get: Mock,  # The mock of `requests.get`, from conftest.py
) -> None:
    """An exception in the request ends the command with exit code 1."""
    mock_requests_get.side_effect = Exception("Boom")
    result = runner.invoke(console.main)
    assert result.exit_code == 1


def test_main_prints_message_on_request_error(
    runner: CliRunner,  # The runner from the fixture
    mock_requests_get: Mock,  # The mock of `requests.get`, from conftest.py
) -> None:
    """A failed request is printed as an error message, not a traceback."""
    mock_requests_get.side_effect = requests.RequestException
    result = runner.invoke(console.main)
    assert "Error" in result.output


@pytest.mark.e2e
def test_main_succeeds_in_production(
    runner: CliRunner,  # The runner from the fixture
) -> None:
    """The command works against the real Wikipedia."""
    result = runner.invoke(console.main)
    assert result.exit_code == 0
