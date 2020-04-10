import unittest
from check_pytest import my_sum
from fractions import Fraction

class MyTest(unittest.TestCase):
    """
    This is test class for testing my_sum function
    """
    def test_sum_of_integers(self):
        """
        Test list sum of list of integers.
        :return:
        """
        data = [1,2,3]
        result = my_sum.my_sum(data)
        #expected_result = 6
        self.assertEqual(result,6)

    def test_sum_of_fractions(self):
        """
        Test list sum of fractions
        :return:
        """
        data = [Fraction(1,4), Fraction(1,4), Fraction(5,9)]
        result = my_sum.my_sum(data)
        self.assertEqual(result,Fraction(19,18))

    def test_sum_of_string_failure_case(self):
        """
        This is test for failure case, when you give string as an input
        :return:
        """
        data = 'banana'
        with self.assertRaises(TypeError):
            result = my_sum.my_sum(data)

if __name__ == '__main__':
    unittest.main()


