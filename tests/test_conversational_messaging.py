import unittest
from src import conversational_messaging

class TestConversationalMessaging(unittest.TestCase):

    def setUp(self):
        self.conversation = conversational_messaging.generate_message()
        self.response_analysis = conversational_messaging.analyze_user_responses()

    def test_generate_message(self):
        self.assertIsNotNone(self.conversation)
        self.assertIsInstance(self.conversation, str)

    def test_analyze_user_responses(self):
        self.assertIsNotNone(self.response_analysis)
        self.assertIsInstance(self.response_analysis, dict)

if __name__ == '__main__':
    unittest.main()