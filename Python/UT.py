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

    

    def test_countingValleys(self):
        self.assertEqual(1, GoodProblems.countingValleys(8, ['UDDDUDUU']))

'''if __name__ == '__main__':
    unittest.main()'''

unittest.main()
