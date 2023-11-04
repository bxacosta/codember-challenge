import unittest
from challenge_01 import decode


class TestChallenges(unittest.TestCase):
    def test_challenge_01(self):
        print("- Test Challenge 01")
        self.assertEqual(decode("keys house HOUSE house keys"), 'keys2house3')
        self.assertEqual(decode("cup te a cup"), 'cup2te1a1')
        self.assertEqual(decode("houses house housess"), 'houses1house1housess1')


if __name__ == '__main__':
    unittest.main()
