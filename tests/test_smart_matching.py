import unittest
from src import smart_matching

class TestSmartMatching(unittest.TestCase):

    def setUp(self):
        self.smart_matcher = smart_matching.SmartMatcher()

    def test_smart_match(self):
        user_preferences = {"age_range": [25, 35], "location": "New York", "interests": ["music", "sports"]}
        swiping_patterns = {"likes": 70, "dislikes": 30}
        historical_data = {"previous_matches": 50, "successful_conversations": 25}
        
        result = self.smart_matcher.smart_match(user_preferences, swiping_patterns, historical_data)
        self.assertIsInstance(result, list)

    def test_improve_matching_accuracy(self):
        user_feedback = {"likes": 70, "dislikes": 30, "matches": 50, "successful_conversations": 25}
        result = self.smart_matcher.improve_matching_accuracy(user_feedback)
        self.assertIsInstance(result, dict)

if __name__ == '__main__':
    unittest.main()