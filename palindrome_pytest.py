import palindrome
import pytest


# No need for classes or anything with PyTest, just make functions with regular asserts
def test_palindrome():
    assert palindrome.is_palindrome("Madam")
    assert palindrome.is_palindrome("racecar")


# Not palindrome test
def test_not_palindrome():
    assert palindrome.is_palindrome("Bruh") == False
    assert palindrome.is_palindrome("SHEESH") == False


# Invalid input test (integers, floats)
def test_invalid():
    assert palindrome.is_palindrome(123) == False
    assert palindrome.is_palindrome(-100.420) == False