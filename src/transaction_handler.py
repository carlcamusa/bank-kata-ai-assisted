from typing import List
from src.transaction import Transaction
from src.clock import Clock

class TransactionHandler:
    def __init__(self, clock: Clock) -> None:
        self._clock: Clock = clock
        self._transactions: List[Transaction] = []
        self._current_balance: int = 0

    def add_transaction(self, amount: int) -> None:
        date_str: str = self._clock.today_as_string()
        self._current_balance += amount
        transaction = Transaction(date=date_str, amount=amount, balance=self._current_balance)
        self._transactions.append(transaction)

    def get_all_transactions_for_statement(self) -> List[Transaction]:
        # Returns a reversed copy for statement printing (newest first)
        return self._transactions[::-1] 