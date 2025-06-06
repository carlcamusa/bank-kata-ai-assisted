from typing import List
from src.transaction import Transaction
from src.clock import Clock
from src.transaction_ledger import TransactionLedger

class TransactionHandler:
    def __init__(self, clock: Clock) -> None:
        self._clock: Clock = clock
        self._ledger: TransactionLedger = TransactionLedger()

    def add_transaction(self, amount: int) -> None:
        date_str: str = self._clock.today_as_string()
        self._ledger.add(date_str=date_str, amount=amount)

    def get_all_transactions_for_statement(self) -> List[Transaction]:
        return self._ledger.get_all_reversed() 