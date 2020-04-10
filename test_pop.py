import unittest
import pop_me

class MyTestCase(unittest.TestCase):
    def test_pop(self):
        my_list = [1, 2, 3]
        result = pop_me.pop_me(my_list)
        self.assertEqual(result, [1, 2])


if __name__ == '__main__':
    unittest.main()
