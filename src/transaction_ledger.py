from typing import List
from src.transaction import Transaction

class TransactionLedger:
    def __init__(self) -> None:
        self._transactions: List[Transaction] = []
        self._current_balance: int = 0

    def add(self, date_str: str, amount: int) -> None:
        """Adds a new transaction to the ledger and updates the balance."""
        self._current_balance += amount
        transaction = Transaction(date=date_str, amount=amount, balance=self._current_balance)
        self._transactions.append(transaction)

    def get_all_reversed(self) -> List[Transaction]:
        """Returns a list of all transactions in reverse chronological order."""
        return self._transactions[::-1] 