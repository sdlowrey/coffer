import click


class Strings:
    short_help = 'fixme short help'


@click.command()
@click.argument('path')
def coffer(path: str):
    click.echo('path: {}'.format(path))
