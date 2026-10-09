"""Tests of the library, wikirandom."""

from unittest.mock import Mock

import pytest
import wikirandom


def test_random_page_uses_given_language(
    mock_requests_get: Mock,  # The mock of `requests.get`, from conftest.py
) -> None:
    """The language chooses the Wikipedia that is asked."""
    wikirandom.random_page(language="es")
    args, _ = mock_requests_get.call_args
    assert "es.wikipedia.org" in args[0]


@pytest.mark.e2e
def test_random_page_returns_page_in_production() -> None:
    """The real Wikipedia's answer makes a Page."""
    page = wikirandom.random_page()
    assert isinstance(page, wikirandom.Page)


def test_random_page_handles_validation_error(
    mock_requests_get: Mock,  # The mock of `requests.get`, from conftest.py
) -> None:
    """An answer that is not a page raises WikipediaError."""
    mock_requests_get.return_value.__enter__.return_value.json.return_value = {}
    with pytest.raises(wikirandom.WikipediaError):
        wikirandom.random_page()
