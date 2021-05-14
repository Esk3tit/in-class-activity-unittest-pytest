# Check if a string is a palindrome or not
# by seeing if the string and its reverse are equal
# since palindromes read the same forward and backward
def is_palindrome(s):

    # Find the reversed string, using splicing starting from the end
    rev = s[::-1]

    # Check for equality between original forward string and reverse string
    # We make sure to check lowercase version so that case doesn't matter for the string
    if s.lower() == rev.lower():

        # True then it is palindrome
        return True

    else:

        return False
