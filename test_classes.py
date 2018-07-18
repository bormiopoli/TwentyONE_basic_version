import unittest
from classes import Bank, Table, Player

class rulesTest(unittest.TestCase):
    """Tests for `classes.py`."""

    def test_Bank(self):
        self.assertTrue(Bank())
        self.assertIs(Bank().points, 0)
        self.assertFalse(Bank().status)
        self.assertIsNone(Bank().action)
        self.assertEqual(Bank().cards, [])

    def test_Player(self):
        self.assertEqual(Player().name, "No name")
        self.assertEqual(Player().cards, [])
        self.assertEqual(Player().points, 0)
        self.assertEqual(Player().balance, 0)
        self.assertFalse(Player().status)
        self.assertIsNone(Player().action)

    def test_Table(self):
        self.assertEqual(Table().players,[])
        self.assertEqual(Table().id,0)
        self.assertEqual(Table().hand,[])


if __name__ == '__main__':
    unittest.main()