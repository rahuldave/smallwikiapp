"""The wikiapp command."""

import textwrap

import click
from wikirandom import WikipediaError, random_page

from wikiapp import __version__


@click.command()
@click.option(
    "--language",
    "-l",
    default="en",
    help="The language of the Wikipedia to ask, as its code: en, fr, es",
    metavar="LANG",
    show_default=True,
)
@click.version_option(version=__version__)
def main(
    language: str,  # The language of the Wikipedia to ask, from --language
) -> None:
    """Print the title and summary of a random Wikipedia page, in the language asked for.

    The title is in green, and the summary is wrapped to 70 columns.
    """
    try:
        page = random_page(language=language)
    except WikipediaError as error:
        raise click.ClickException(str(error)) from error
    click.secho(page.title, fg="green")
    click.echo(textwrap.fill(page.extract))


if __name__ == "__main__":
    main()
