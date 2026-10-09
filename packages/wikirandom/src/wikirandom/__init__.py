"""wikirandom: a random page of Wikipedia, in any language, from its REST API."""

import importlib.metadata
import re

import requests
from pydantic import BaseModel, ValidationError

API_URL = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"
LANGUAGE = re.compile(r"[a-z]+(-[a-z]+)*")  # en, fr, simple, zh-yue: letters and hyphens
VERSION = importlib.metadata.version("wikirandom")
USER_AGENT = f"wikirandom/{VERSION} (https://github.com/rahuldave/smallwikiapp)"


class WikipediaError(Exception):
    """Wikipedia could not give a page."""


class Page(BaseModel):
    """A page of Wikipedia: its title and the summary of its text."""

    title: str  # The title of the page
    extract: str  # The summary: the first paragraph of the page, as plain text


def random_page(
    language: str = "en",  # The language of the Wikipedia to ask, as its code: en, fr, es
) -> Page:  # A page chosen at random
    """Get a random page from Wikipedia.

    Raises WikipediaError when the language is not a language code, when the request fails, or
    when the answer is not a page.
    """
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
