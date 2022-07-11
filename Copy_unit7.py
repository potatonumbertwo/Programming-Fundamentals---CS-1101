alphabet = "abcdefghijklmnopqrstuvwxyz"
test_dups = ["zzz", "dog", "bookkeeper", "subdermatoglyphic", "subdermatoglyphics"]
test_miss = ["zzz", "subdermatoglyphic", "the quick brown fox jumps over the lazy dog"]


# From Section 11.2 of: 
# Downey, A. (2015). Think Python: How to think like a computer scientist.
# Needham, Massachusetts: Green Tree Press. 

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


# print(histogram())

def has_duplicates(string_to_analyze):
    """ define a function called has_duplicates that takes a string parameter and
    returns True if the string has any repeated characters. Otherwise,return False"""
    for i in test_dups:
        histogram(i)
        print(i)
        return True
    else:
        return False


print(has_duplicates('zzz'))


def missing_letters(new_string):
    """ define a function called missing_letters that takes a string parameter
    and returns a new string with fileNamesList the letters of the alphabet
    that are not in the argument string.
    The letters in the returned string should be in alphabetical order."""
    filter_letter = []
    for i in new_string:
        if i not in new_string:
            filter_letter.append()
