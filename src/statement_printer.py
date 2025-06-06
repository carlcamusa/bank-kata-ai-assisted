from typing import List
from src.transaction import Transaction

class StatementPrinter:
    def print_statement(self, transactions: List[Transaction]) -> None:
        """Prints the statement header and all transactions."""
        print("DATE | AMOUNT | BALANCE")
        for transaction in transactions:
            # Transactions are provided in reverse chronological order by TransactionHandler
            print(f"{transaction.date} | {transaction.amount} | {transaction.balance}") 