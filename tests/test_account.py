import unittest
from unittest.mock import patch, MagicMock
from src.account import Account
# Assuming Transaction is imported in Account or its collaborators, 
# but for test data, we might not need a real Transaction object if just passing it through.
# from src.transaction import Transaction # Not strictly needed if mocks handle everything

# Apply patches at the class level
@patch('src.account.StatementPrinter')      # Outermost decorator, becomes the last mock argument
@patch('src.account.TransactionHandler')   # Middle decorator, becomes the middle mock argument
@patch('src.account.SystemClock')         # Innermost decorator, becomes the first mock argument
class TestAccount(unittest.TestCase):

    def test_account_initialization(
        self,
        mock_system_clock_class: MagicMock,        # From @patch('src.account.SystemClock')
        mock_transaction_handler_class: MagicMock, # From @patch('src.account.TransactionHandler')
        mock_statement_printer_class: MagicMock  # From @patch('src.account.StatementPrinter')
    ) -> None:
        """Test that Account initializes its collaborators correctly."""
        mock_clock_instance = MagicMock()
        mock_system_clock_class.return_value = mock_clock_instance
        mock_th_instance = MagicMock()
        mock_transaction_handler_class.return_value = mock_th_instance
        mock_sp_instance = MagicMock()
        mock_statement_printer_class.return_value = mock_sp_instance

        account = Account()

        mock_system_clock_class.assert_called_once_with()
        mock_transaction_handler_class.assert_called_once_with(mock_clock_instance)
        mock_statement_printer_class.assert_called_once_with()
        self.assertIs(account._transaction_handler, mock_th_instance)
        self.assertIs(account._statement_printer, mock_sp_instance)

    def test_deposit_positive_amount(
        self,
        mock_system_clock_class: MagicMock,
        mock_transaction_handler_class: MagicMock,
        mock_statement_printer_class: MagicMock
    ) -> None:
        """Test that depositing a positive amount calls transaction_handler.add_transaction."""
        mock_th_instance = MagicMock()
        mock_transaction_handler_class.return_value = mock_th_instance # Use passed-in mock
        mock_system_clock_class.return_value = MagicMock() # Use passed-in mock
        mock_statement_printer_class.return_value = MagicMock() # Use passed-in mock

        account = Account()
        deposit_amount = 500
        account.deposit(deposit_amount)
        mock_th_instance.add_transaction.assert_called_once_with(deposit_amount)

    def test_withdraw_positive_amount(
        self,
        mock_system_clock_class: MagicMock,
        mock_transaction_handler_class: MagicMock,
        mock_statement_printer_class: MagicMock
    ) -> None:
        """Test that withdrawing a positive amount calls transaction_handler.add_transaction with a negative value."""
        mock_th_instance = MagicMock()
        mock_transaction_handler_class.return_value = mock_th_instance # Use passed-in mock
        mock_system_clock_class.return_value = MagicMock() # Use passed-in mock
        mock_statement_printer_class.return_value = MagicMock() # Use passed-in mock

        account = Account()
        withdrawal_amount = 100
        account.withdraw(withdrawal_amount)
        mock_th_instance.add_transaction.assert_called_once_with(-withdrawal_amount)

    def test_print_statement_calls_collaborators(
        self,
        mock_system_clock_class: MagicMock,
        mock_transaction_handler_class: MagicMock,
        mock_statement_printer_class: MagicMock
    ) -> None:
        """Test that print_statement fetches transactions and calls statement_printer."""
        mock_th_instance = MagicMock()
        mock_transaction_handler_class.return_value = mock_th_instance # Use passed-in mock
        mock_sp_instance = MagicMock()
        mock_statement_printer_class.return_value = mock_sp_instance # Use passed-in mock
        mock_system_clock_class.return_value = MagicMock() # Use passed-in mock (for __init__)

        dummy_transactions = [MagicMock(), MagicMock()]
        mock_th_instance.get_all_transactions_for_statement.return_value = dummy_transactions

        account = Account()
        account.print_statement()

        mock_th_instance.get_all_transactions_for_statement.assert_called_once_with()
        mock_sp_instance.print_statement.assert_called_once_with(dummy_transactions)

if __name__ == '__main__':
    unittest.main() 