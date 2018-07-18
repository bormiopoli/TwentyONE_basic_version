import unittest
from rules import pick_card, remove_card, check_tables, shuffle_cards, sum_points


class RulesTest(unittest.TestCase):
    """Tests for `rules.py`."""

    def test_pick_card(self):
        """Is 10 successfully picked"""
        self.assertEqual(pick_card([10, 10]), 10)

    def test_remove_card(self):
        self.assertTrue(remove_card([10, 10], 10))

    def test_check_tables(self):
        # 5 players take 2 tables
        self.assertEqual(check_tables(5), 2)

    def test_shuffle_cards(self):
        self.assertTrue(shuffle_cards())

    def test_sum_points(self):
        # 5 + 5 = 10
        self.assertIs(sum_points(5, 5), 10)


if __name__ == '__main__':
    unittest.main()