import click
from wikiapp import __version__
import textwrap

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
def main(language) -> None:
    """Print the title and summary of a random Wikipedia page."""
    try:
        data = random_page(language=language)
    except WikipediaError as error:
        raise click.ClickException(str(error)) from error
    title = data["title"]
    extract = data["extract"]
    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))

if __name__=="__main__":
    main()
