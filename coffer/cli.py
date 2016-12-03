import click


class Strings:
    get_help = 'Retrieve and decrypt a file'
    list_help = 'List stored files'
    main_help = 'Encrypt and store files in Amazon S3'
    put_help = 'Encrypt and store a file'
    remove_help = 'Remove a file from storage'


@click.group(help=Strings.main_help)
def cli():
    pass


@cli.command(short_help=Strings.get_help)
def get():
    click.echo('get')


@cli.command(short_help=Strings.list_help)
def ls():
    click.echo('list')


@cli.command(short_help=Strings.put_help)
def put():
    click.echo('put')


@cli.command(short_help=Strings.remove_help)
def rm():
    click.echo('remove')
