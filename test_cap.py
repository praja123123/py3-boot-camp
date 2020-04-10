import unittest
import cap


class MyTestCase(unittest.TestCase):
    def test_one_word(self):
        text = 'dupa'
        result = cap.cap(text)
        self.assertEqual(result, 'Dupa')


if __name__ == '__main__':
    unittest.main()
