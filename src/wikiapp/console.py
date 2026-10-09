import click
from wikiapp import __version__
import textwrap

from wikiapp.wikipedia import random_page

@click.command()
@click.version_option(version=__version__)
def main() -> None:
    """Print the title and summary of a random Wikipedia page."""
    data = random_page()
    title = data["title"]
    extract = data["extract"]
    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))

if __name__=="__main__":
    main()
