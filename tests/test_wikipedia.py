"""Tests of the library, wikipedia.py."""

from unittest.mock import Mock

import pytest

from wikiapp import wikipedia


def test_random_page_uses_given_language(
    mock_requests_get: Mock,  # The mock of `requests.get`, from conftest.py
) -> None:
    """The language chooses the Wikipedia that is asked."""
    wikipedia.random_page(language="es")
    args, _ = mock_requests_get.call_args
    assert "es.wikipedia.org" in args[0]


@pytest.mark.e2e
def test_random_page_returns_page_in_production() -> None:
    """The real Wikipedia's answer makes a Page."""
    page = wikipedia.random_page()
    assert isinstance(page, wikipedia.Page)


def test_random_page_handles_validation_error(
    mock_requests_get: Mock,  # The mock of `requests.get`, from conftest.py
) -> None:
    """An answer that is not a page raises WikipediaError."""
    mock_requests_get.return_value.__enter__.return_value.json.return_value = {}
    with pytest.raises(wikipedia.WikipediaError):
        wikipedia.random_page()
