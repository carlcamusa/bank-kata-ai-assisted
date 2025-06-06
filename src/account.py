from src.transaction_handler import TransactionHandler
from src.statement_printer import StatementPrinter
from src.clock import SystemClock

class Account:
    def __init__(self) -> None:
        # As per CRC, Account collaborates with TransactionHandler and StatementPrinter.
        # It instantiates its own dependencies for now.
        self._transaction_handler: TransactionHandler = TransactionHandler(SystemClock())
        self._statement_printer: StatementPrinter = StatementPrinter()

    def deposit(self, amount: int) -> None:
        """Deposits the given amount into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._transaction_handler.add_transaction(amount)

    def withdraw(self, amount: int) -> None:
        """Withdraws the given amount from the account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        self._transaction_handler.add_transaction(-amount) # Negative for withdrawal

    def print_statement(self) -> None:
        """Prints the account statement to the console."""
        transactions = self._transaction_handler.get_all_transactions_for_statement()
        self._statement_printer.print_statement(transactions) 