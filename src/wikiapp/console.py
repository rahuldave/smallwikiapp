import click
from wikiapp import __version__
import requests
import textwrap

API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
USER_AGENT = "wikiapp/0.1.0 (https://github.com/rahuldave/smallwikiapp)"

@click.command()
@click.version_option(version=__version__)
def main() -> None:
    """Print the title and summary of a random Wikipedia page."""
    with requests.get(API_URL, headers={"User-Agent": USER_AGENT}) as response:
        response.raise_for_status()
        data = response.json()
        title = data["title"]
        extract = data["extract"]
        click.secho(title, fg="green")
        click.echo(textwrap.fill(extract))

if __name__=="__main__":
    main()
