from unittest.mock import patch, call
from src.account import Account

class TestAccountStatement:
    def test_should_print_statement_containing_all_transactions(self) -> None:
        account = Account()
        account.deposit(1000)
        account.withdraw(100)
        account.deposit(500)

        with patch("builtins.print") as mock_print:
            account.print_statement()

        expected_calls = [
            call("DATE | AMOUNT | BALANCE"),
            call("10/04/2014 | 500 | 1400"),
            call("02/04/2014 | -100 | 900"),
            call("01/04/2014 | 1000 | 1000"),
        ]
        mock_print.assert_has_calls(expected_calls) 