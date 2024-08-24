import unittest
from unittest.mock import patch, MagicMock
from error_handling.error_logger import log_error
from error_handling.retry_handler import retry_on_failure

class TestErrorHandling(unittest.TestCase):

    @patch('error_handling.error_logger.logging.error')
    def test_log_error(self, mock_log_error):
        log_error("Test error")
        mock_log_error.assert_called_once_with("Test error")

    @patch('error_handling.retry_handler.time.sleep', return_value=None)
    def test_retry_on_failure_success(self, mock_sleep):
        func = MagicMock(return_value="Success")
        result = retry_on_failure(func, max_retries=3, delay=1)
        
        self.assertEqual(result, "Success")
        func.assert_called_once()

    @patch('error_handling.retry_handler.time.sleep', return_value=None)
    def test_retry_on_failure_fail(self, mock_sleep):
        func = MagicMock(side_effect=Exception("Test error"))
        result = retry_on_failure(func, max_retries=3, delay=1)
        
        self.assertIsNone(result)
        self.assertEqual(func.call_count, 3)

if __name__ == '__main__':
    unittest.main()
