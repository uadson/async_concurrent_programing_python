import typer
from typing import Optional
from rich.console import Console
from rich.table import Table
from rich import print


from insecure_data.core import add_account_to_database, get_accounts_from_database


main = typer.Typer(help='Account Management Application')
console = Console()


@main.command()
def add(
    balance: float = typer.Option(...),
):
    """Adds a new account to the database"""
    if add_account_to_database(balance):
        print(':account_mug: Account added!')
    else:
        print(':no_entry: - Cannot add account.')


@main.command('list')
def list_accounts(style: Optional[str] = None):
    """Lists accounts from the database"""
    accounts = get_accounts_from_database(style)
    table = Table(
        title='Account Database' if not style else f'Account {style}'
    )
    
    headers = [
        'id',
        'balance',
        'date',
    ]

    for header in headers:
        table.add_column(header, style='magenta')
    for account in accounts:
        account.date = account.date.strftime("%Y-%m-%d")
        values = [str(getattr(account, header)) for header in headers]
        table.add_row(*values)
    console.print(table)
