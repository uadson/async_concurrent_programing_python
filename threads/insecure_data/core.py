from typing import Optional, List
from sqlmodel import select
from database import get_session
from models import Account


def add_account_to_database(
    balance: int,
) -> bool:
    with get_session() as session:
        account = Account(**locals())
        session.add(account)
        session.commit()

    return True


def get_accounts_from_database(style: Optional[str] = None) -> List[Account]:
    with get_session() as session:
        sql = select(Account)
        if style:
            sql = sql.where(Account.style == style)
        return list(session.exec(sql))
