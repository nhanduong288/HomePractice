import unittest
import GoodProblems

class TestGoodProblems(unittest.TestCase):
    def test_digits(self):
        self.assertEqual(1, GoodProblems.digits(0))
        self.assertEqual(2, GoodProblems.digits(25))
        self.assertEqual(3, GoodProblems.digits(123))

    def test_counter(self):
        self.assertEqual("Counting up: 1,2,3,4,5,6,7,8,9,10", GoodProblems.counter(1,10))

    def test_kangaroo(self):
        self.assertEqual("YES", GoodProblems.kangaroo(0, 3, 4, 2))
        self.assertEqual("YES", GoodProblems.kangaroo(14, 4, 98, 2))
        self.assertEqual("NO", GoodProblems.kangaroo(21, 6, 47, 3))
        self.assertEqual("NO", GoodProblems.kangaroo(0, 2, 5, 3))

    def test_getTotalX(self):
        self.assertEqual(3, GoodProblems.getTotalX([2, 4], [16, 32, 96]))

    def test_breakingRecords(self):
        self.assertEqual((2, 4), GoodProblems.breakingRecords(
            [10, 5, 20, 20, 4, 5, 2, 25, 1]))

    def test_birthday(self):
        self.assertEqual(2, GoodProblems.birthday([1, 2, 1, 3, 2], 3, 2))
        self.assertEqual(0, GoodProblems.birthday([1, 1, 1, 1, 1, 1], 3, 2))
        self.assertEqual(1, GoodProblems.birthday([4], 4, 1))

    def test_countingValleys(self):
        self.assertEqual(1, GoodProblems.countingValleys(8, ['UDDDUDUU']))

'''if __name__ == '__main__':
    unittest.main()'''

unittest.main()
