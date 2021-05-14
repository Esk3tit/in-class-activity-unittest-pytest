import palindrome
import unittest


class PalindromeClass(unittest.TestCase):

    # Palindrome test
    def test_palindrome(self):
        self.assertEqual(palindrome.is_palindrome("Madam"), True)
        self.assertEqual(palindrome.is_palindrome("racecar"), True)

    # Not palindrome test
    def test_not_palindrome(self):
        self.assertEqual(palindrome.is_palindrome("Bruh"), False)
        self.assertEqual(palindrome.is_palindrome("SHEESH"), False)

    # Invalid input test (integers, floats)
    def test_invalid(self):
        self.assertEqual(palindrome.is_palindrome(123), False)
        self.assertEqual(palindrome.is_palindrome(-100.420), False)


if __name__ == "__main__":
    unittest.main()
