import unittest

def adding_one(num):
    """
    Function is adding one to given number.

    :param num:
    :return: num +1

    >>> adding_one(9)
    10
    >>> adding_one(0)
    1
    """
    return num + 1

def test_answer():
    assert adding_one(6) == 7

class Test(unittest.TestCase):
    def test_adding_one(self):
        self.assertEqual(adding_one(3), 5)


if __name__ == '__main__':
    unittest.main()
    #import doctest
    #doctest.testmod()

