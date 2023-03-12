import unittest

from src.high_scores import highest_to_lowest, latest, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    # Test latest score (the last thing in the list)
    def test_latest_score(self):
        self.assertEqual(100, latest([30, 50, 29, 100]))


    def test_personal_best(self):
        self.assertEqual(500, personal_best([300,200,250,500]))

    # Test personal best (the highest score in the list)

    #  Test top three from list of scores

    def test_personal_top_three(self):
        self.assertEqual([5,4,3], personal_top_three([1,2,3,4,5]))


    # # Test ordered from highest to lowest
    def test_high_to_low(self):
        self.assertEqual([5,4,3,2,1], highest_to_lowest([1,2,3,4,5]))

    # Test top three when there is a tie

    def test_top_three_when_there_is_a_tie(self):
        self.assertEqual([5,4,3], top_three_in_tie[1,2,3,4,4,5])

    # Test top three when there are less than three

    # Test top three when there is only one

