import unittest
from unittest.mock import Mock
from Email import EmailSender

class TestEmailSender(unittest.TestCase):
    def test_email_sender(self):
        mock_email_sender = Mock(spec=EmailSender)
        
        mock_email_sender.send_email.return_value = "Mock email sent!"
        
        response = mock_email_sender.send_email("example@example.com", "Hello, this is a test email.")
        mock_email_sender.send_email.assert_called_once_with("example@example.com", "Hello, this is a test email.")
        
        self.assertEqual(response, "Mock email sent!")

if __name__ == '__main__':
    unittest.main()

