import word_count
import unittest


class WordCountClass(unittest.TestCase):

    # Word count test for regular sentences
    def test_easy(self):
        self.assertEqual(word_count.wc("This is four words"), 4)
        self.assertEqual(word_count.wc("Bruh moment"), 2)
        self.assertEqual(word_count.wc("This is kinda lit fam ngl"), 6)

    # Edge cases (test with numbers in string and special characters)
    def test_edge(self):
        self.assertEqual(word_count.wc("This is 4 words"), 4)
        self.assertEqual(word_count.wc("We got special character @ here!"), 6)
        self.assertEqual(word_count.wc("    "), 0)

    # Clearly invalid cases (integer input)
    def test_invalid(self):
        self.assertEqual(word_count.wc(420), 3)
        self.assertEqual(word_count.wc(-123456), 6)


if __name__ == "__main__":
    unittest.main()
