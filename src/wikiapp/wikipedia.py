import re

import requests
from pydantic import BaseModel, ValidationError

API_URL = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"
LANGUAGE = re.compile(r"[a-z]+(-[a-z]+)*")  # en, fr, simple, zh-yue: letters and hyphens
USER_AGENT = "wikiapp/0.1.0 (https://github.com/rahuldave/smallwikiapp)"


class WikipediaError(Exception):
    """Wikipedia could not give a page."""


class Page(BaseModel):
    """A page of Wikipedia: its title and the summary of its text."""

    title: str
    extract: str


def random_page(language: str = "en") -> Page:
    """Get a random page from Wikipedia."""
    if not LANGUAGE.fullmatch(language):
        raise WikipediaError(f"{language!r} is not a language code, such as en, fr or zh-yue")
    try:
        with requests.get(
            API_URL.format(language=language), headers={"User-Agent": USER_AGENT}, timeout=10
        ) as response:
            response.raise_for_status()
            return Page.model_validate(response.json())
    except (requests.RequestException, ValidationError) as error:
        raise WikipediaError(str(error)) from error
