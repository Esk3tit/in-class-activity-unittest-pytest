# Word count by iterating through a string until you reach end of string
# Every iteration should stop at whitespace which counts all the text before
# the whitespace as a word
def wc(s):

    # Use the split function
    # split splits the string into a list of iterables
    # with space as the delimiter (turns string into list of words)
    # We just need the number of elements in the list or the length for the word count
    return len(s.split())
