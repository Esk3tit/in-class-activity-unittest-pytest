import word_count
import pytest


# Word count test for regular sentences
def test_easy():
    assert word_count.wc("This is four words") == 4
    assert word_count.wc("Bruh moment") == 2
    assert word_count.wc("This is kinda lit fam ngl") == 6


# Edge cases (test with numbers in string and special characters)
def test_edge():
    assert word_count.wc("This is 4 words") == 4
    assert word_count.wc("We got special character @ here!") == 6
    assert word_count.wc("    ") == 0


# Clearly invalid cases (integer input)
def test_invalid():
    assert word_count.wc(420) == 3
    assert word_count.wc(-123456) == 6
