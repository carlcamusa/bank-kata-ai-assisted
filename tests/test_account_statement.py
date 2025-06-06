import datetime as datetime_module
from unittest.mock import patch, call
from src.account import Account

OriginalDateTime = datetime_module.datetime # Store original datetime class

class TestAccountStatement:
    @patch('src.clock.datetime.datetime')
    def test_should_print_statement_containing_all_transactions(self, mock_datetime_class_in_clock) -> None: # Renamed for clarity
        # Use OriginalDateTime to create real datetime objects
        mock_dt_1 = OriginalDateTime(2014, 4, 1)
        mock_dt_2 = OriginalDateTime(2014, 4, 2)
        mock_dt_3 = OriginalDateTime(2014, 4, 10)
        
        # Configure the 'now' method of the mocked class in src.clock
        mock_datetime_class_in_clock.now.side_effect = [mock_dt_1, mock_dt_2, mock_dt_3]

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