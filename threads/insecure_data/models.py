import threading
import random
import time

from typing import List

from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
# from pydantic import validator
# from statistics import mean


class Account(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    balance: int = 0
    date: datetime = Field(default_factory=datetime.now)


account = Account(balance=random.randint(5_000, 10_000))

def main():
    accounts = create_account()
    total = sum(account.balance for account in accounts)
    print('Initiating transfers ...')

    tasks = [
        threading.Thread(target=services, args=(accounts, total)),
        # threading.Thread(target=services, args=(accounts, total)),
    ]

    [task.start() for task in tasks]
    [task.join() for task in tasks]

    print('Complete Transfers.')

    validate_account(accounts, total)


def services(accounts, total):
     for _ in range(1, 10_001):
         ac1, ac2 = get_two_accounts(accounts)
         value = random.randint(1, 100)
         transfer(ac1, ac2, value)
         validate_account(accounts, total)


def create_account() -> List[Account]:
    return [
        Account(balance=random.randint(5_000, 10_000)),
        Account(balance=random.randint(5_000, 10_000)),
        Account(balance=random.randint(5_000, 10_000)),
        Account(balance=random.randint(5_000, 10_000)),
        Account(balance=random.randint(5_000, 10_000)),
        Account(balance=random.randint(5_000, 10_000)),
    ]


def transfer(origin:Account, destin:Account, value:int):
    if origin.balance < value:
        return 
    origin.balance -= value
    time.sleep(0.001)
    destin.balance += value


def validate_account(accounts:List[Account], total:int):
    current = sum(account.balance for account in accounts)

    if current != total:
        print(f'ERROR: inconsistent bank balance. BRL$ {current:.2f} vs {total:.2f}', flush=True)
    else:
        print(f'ALL OK: consistent bank balance. BRL$ {total:.2f}', flush=True)


def get_two_accounts(accounts):
    ac1 = random.choice(accounts)
    ac2 = random.choice(accounts)

    while ac1 == ac2:
        ac2 = random.choice(accounts)

    return ac1, ac2


if __name__ == '__main__':
    main()
 