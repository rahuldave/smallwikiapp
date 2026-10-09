import textwrap

import click

from wikiapp import __version__
from wikiapp.wikipedia import WikipediaError, random_page


@click.command()
@click.option(
    "--language",
    "-l",
    default="en",
    help="Gets random page from Wikipedia in given language",
    metavar="LANG",
    show_default=True,
)
@click.version_option(version=__version__)
def main(language: str) -> None:
    """Print the title and summary of a random Wikipedia page."""
    try:
        page = random_page(language=language)
    except WikipediaError as error:
        raise click.ClickException(str(error)) from error
    click.secho(page.title, fg="green")
    click.echo(textwrap.fill(page.extract))


if __name__ == "__main__":
    main()
