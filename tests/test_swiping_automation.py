import unittest
from src import swiping_automation

class TestSwipingAutomation(unittest.TestCase):

    def setUp(self):
        self.swipe = swiping_automation.swipe_automation()
        self.analyze = swiping_automation.analyze_profile_images()

    def test_swipe_automation(self):
        self.assertIsNotNone(self.swipe)
        self.assertIsInstance(self.swipe, dict)
        self.assertIn('age_range', self.swipe)
        self.assertIn('location', self.swipe)
        self.assertIn('interests', self.swipe)

    def test_analyze_profile_images(self):
        self.assertIsNotNone(self.analyze)
        self.assertIsInstance(self.analyze, dict)
        self.assertIn('image_analysis', self.analyze)

if __name__ == '__main__':
    unittest.main()