import requests

API_URL = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"
USER_AGENT = "wikiapp/0.1.0 (https://github.com/rahuldave/smallwikiapp)"

class WikipediaError(Exception):
    """Wikipedia could not give a page."""

def random_page(language="en"):
    """Get a random page from Wikipedia."""
    try:
        with requests.get(API_URL.format(language=language), headers={"User-Agent": USER_AGENT}) as response:
            response.raise_for_status()
            return response.json()
    except requests.RequestException as error:
        raise WikipediaError(str(error)) from error
