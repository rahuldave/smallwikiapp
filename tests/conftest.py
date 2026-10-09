"""What every test file can use: a mock in place of `requests.get`."""

from unittest.mock import Mock

import pytest
from pytest_mock import MockerFixture


@pytest.fixture
def mock_requests_get(
    mocker: MockerFixture,  # pytest-mock's fixture, which undoes every patch after the test
) -> Mock:  # The mock that replaces `requests.get` for the length of one test
    """Replace `requests.get` with a mock that answers with one page, Lorem Ipsum."""
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Lorem Ipsum",
        "extract": "Lorem ipsum dolor sit amet",
    }
    return mock
